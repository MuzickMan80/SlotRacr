from aiohttp import web
import aiohttp_cors
import json
import socketio
from racr.track_manager import TrackManager
from racr.settings.track_settings import load_settings
import app_rest_api

class TrackManagerApp(socketio.AsyncNamespace):
    sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=True)

    def __init__(self, io_manager):
        super().__init__()
        self.track = TrackManager(io_manager, self.emit_lane_dump)
        app_rest_api.track = self.track

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
        load_settings(self.track)
        
    async def stop(self):
        await self.site.stop()
        await self.runner.shutdown()
        await self.runner.cleanup()

    async def emit_lane_dump(self):
        state = {
            "race": { "type": "race", "started": False },
            "lanes": list(map(lambda l: l.state(), self.track.lanes))
        }
        lane_dump = json.dumps(state)
        print(lane_dump)
        await self.emit('update', lane_dump)

    def on_connect(self, sid, environ):
        print('server_connect')

    async def on_update(self, sid):
        print('server_update')
        await self.emit_lane_dump()

    async def on_simulate_activity(self, sid, data):
        print('server_simulate_activity ' + str(data))
        self.track.enable_activity_simulator(data['enable'], data['rate'])
