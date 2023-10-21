import asyncio
from aiohttp import web
import aiohttp_cors
import json
import socketio
from racr.track_manager import TrackManager
from racr.settings.track_settings import load_settings
from racr.station_manager import StationManager
import app_rest_api

class TrackManagerApp(socketio.AsyncNamespace):
    sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=False)

    def __init__(self, io_manager):
        super().__init__()
        self.track_updated = False
        self.track = TrackManager(io_manager, self.on_track_updated)
        self.station_manager = StationManager()
        app_rest_api.track = self.track
        self.running = False

    async def start(self):
        self.webapp = web.Application()
        self.sio.attach(self.webapp)
        self.sio.register_namespace(self)
        self.webapp.add_routes(app_rest_api.routes)
        self.cors = aiohttp_cors.setup(self.webapp, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })
        # Configure CORS on all routes.
        for route in list(self.webapp.router.routes()):
            try:
                self.cors.add(route)
            except Exception as ex:
                print(ex)
        self.runner = web.AppRunner(self.webapp)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, '0.0.0.0', 80)
        await self.site.start()
        await load_settings(self.track)
        self.running = True
        asyncio.get_event_loop().create_task(self.update_emitter_task())
        
    async def stop(self):
        self.running = False
        await self.site.stop()
        await self.runner.shutdown()
        await self.runner.cleanup()

    async def on_track_updated(self):
        self.track_updated = True

    async def update_emitter_task(self):
        while self.running:
            if self.track_updated:
                self.track_updated = False
                await self.emit_lane_dump()
                
            await asyncio.sleep(0.2)

    async def emit_lane_dump(self):
        state = {
            "race": { "type": "race", "started": False, "flag": self.track.flag, "state": self.track.web_state },
            "lanes": list(map(lambda l: l.state(), self.track.lanes))
        }
        lane_dump = json.dumps(state)
        self.station_manager.update(lane_dump)
        await self.emit('update', lane_dump)

    def on_connect(self, sid, environ):
        print('server_connect')

    async def on_update(self, sid):
        print('server_update')
        await self.emit_lane_dump()

    async def on_simulate_activity(self, sid, data):
        print('server_simulate_activity ' + str(data))
        await self.track.enable_activity_simulator(data['enable'], data['rate'])
