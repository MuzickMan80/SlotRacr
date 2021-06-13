import asyncio
import inspect

SECONDS = 1000000

class IoManager:
    def __init__(self):
        self.pins = []
        self.callbacks = []
        self.last_tick = 0

    def _io_update(self, event, edge, tick):
        asyncio.run_coroutine_threadsafe(self._async_io_update(event, edge, tick), asyncio.get_event_loop())

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
