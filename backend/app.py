#!/usr/bin/env python3

import asyncio
from app_server import TrackManagerApp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--target_ip', help='IP Address of the pigpio service', default=None)
parser.add_argument('--mock', help='Mock IO backend', action='store_true')

args = parser.parse_args()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if not args.mock:
        from racr.io.pi_io_manager import PiIoManager
        app = TrackManagerApp(PiIoManager(loop,args.target_ip))
    else:
        from racr.io.fake_io_manager import FakeIoManager
        app = TrackManagerApp(FakeIoManager(loop))

    async def run_app():
        await app.start()
        while True:
            await asyncio.sleep(3600)

    loop.run_until_complete(run_app())
    