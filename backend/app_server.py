from aiohttp import web
import json
import socketio
from racr.track_manager import TrackManager
import app_rest_api

class TrackManagerApp(socketio.AsyncNamespace):
    sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=True)

    def __init__(self, io_manager):
        super().__init__()
        self.track = TrackManager(io_manager, self.emit_lane_dump)
        app_rest_api.track = self.track

    async def start(self):
        self.webapp = web.Application()
        self.webapp.add_routes(app_rest_api.routes)
        self.sio.attach(self.webapp)
        self.sio.register_namespace(self)
        self.runner = web.AppRunner(self.webapp)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, '0.0.0.0', 5000)
        await self.site.start()
        
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