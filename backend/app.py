#!/usr/bin/env python3

import asyncio
import os
from app_server import TrackManagerApp

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if os.name == "posix":
        from racr.io.pi_io_manager import PiIoManager
        app = TrackManagerApp(PiIoManager(loop))  
    else:
        from racr.io.fake_io_manager import FakeIoManager
        app = TrackManagerApp(FakeIoManager(loop))

    async def run_app():
        await app.start()
        while True:
            await asyncio.sleep(3600)

    loop.run_until_complete(run_app())
    