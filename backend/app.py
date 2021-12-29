#!/usr/bin/env python3

import asyncio
import os
from app_server import TrackManagerApp

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if os.name == "posix":
        reset_pin = 4
        lane_pins = [17,27,22,5,6,13,19,26]

        from racr.io.pi_io_manager import PiIoManager
        app = TrackManagerApp(PiIoManager(loop), reset_pin, lane_pins)  
    else:
        from racr.io.fake_io_manager import FakeIoManager
        app = TrackManagerApp(FakeIoManager(), 1, [2,3,4,5,6,7,8,9])

    async def run_app():
        await app.start()
        while True:
            await asyncio.sleep(3600)

    loop.run_until_complete(run_app())
    