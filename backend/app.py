#!/usr/bin/env python3

from aiohttp import web
import json
import socketio
from .track_manager import TrackManager

class TrackManagerApp(socketio.AsyncNamespace):
    sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=True)

    def __init__(self, io_manager, reset_pin, lane_pins):
        super().__init__()
        self.track = TrackManager(io_manager, reset_pin, lane_pins, self.emit_lane_dump)

    async def start(self):
        self.webapp = web.Application()
        self.sio.attach(self.webapp)
        self.sio.register_namespace(self)
        self.runner = web.AppRunner(self.webapp)
        await self.runner.setup()
        site = web.TCPSite(self.runner, 'localhost', 5000)
        await site.start()
        
    async def stop(self):
        await self.runner.cleanup()

    async def emit_lane_dump(self):
        lane_dump = json.dumps(list(
            map(lambda l: l.state(), self.track.lanes)))
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

if __name__ == '__main__':
    reset_pin = 5
    lane_pins = [6,13,19,22,27,17,4,26]

    from .pi_io_manager import PiIoManager
    app = TrackManagerApp(PiIoManager(), reset_pin, lane_pins)
    app.run()