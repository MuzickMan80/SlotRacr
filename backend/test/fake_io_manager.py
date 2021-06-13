import asyncio
from ..io_manager import IoManager

class FakeIoManager(IoManager):
    def __init__(self):
        IoManager.__init__(self)

    async def invoke_callback(self, pin, tick):
        self._io_update(pin, 0, tick)
        await asyncio.sleep(0.001)

    def monitor_pin(self, pin, cb, rising=True, falling=False, pullUp=False, pullDown=True):
        self._register_callback(pin, cb)

    def tick_diff(self, start, end):
        return end-start