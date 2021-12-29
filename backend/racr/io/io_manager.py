import asyncio
import inspect

SECONDS = 1000000

class IoManager:
    def __init__(self, async_loop):
        self.pins = []
        self.callbacks = []
        self.last_tick = 0
        self.async_loop = async_loop

    def get_lane_pin(self, lane) -> int:
        return -1

    def get_reset_pin(self) -> int:
        return -1

    def get_pit_pin(self, lane) -> int:
        return -1

    def _io_update(self, event, edge, tick):
        asyncio.run_coroutine_threadsafe(self._async_io_update(event, edge, tick), self.async_loop)

    async def _async_io_update(self, event, edge, tick):
        self.last_tick = tick
        idx = self.pins.index(event)
        cb = self.callbacks[idx]
        result = cb(edge, tick)
        if inspect.isawaitable(result):
            await result

    def _register_callback(self, pin, cb):
        self.callbacks = self.callbacks + [cb]
        self.pins = self.pins + [pin]
