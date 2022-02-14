import asyncio
import inspect
from .button import Button
from racr.lane_controller.lane_controller import LaneController

SECONDS = 1000000

class IoManager:
    def __init__(self, async_loop):
        self.pins = []
        self.callbacks = []
        self.buttons = []
        self.last_tick = 0
        self.async_loop = async_loop

    def current_ticks(self):
        return self.last_tick

    def get_lane_pin(self, lane) -> int:
        return -1

    def monitor_lane_pin(self, lane, cb):
        self.monitor_pin(self.get_lane_pin(lane), cb)

    def get_reset_pin(self) -> int:
        return -1

    def monitor_reset_pin(self, cb):
        self.buttons.append(Button(self, self.get_reset_pin(), cb))

    def get_pit_pin(self, lane) -> int:
        return -1

    def _io_update(self, event, edge, tick):
        asyncio.run_coroutine_threadsafe(self._async_io_update(event, edge, tick), self.async_loop)

    async def _async_io_update(self, event, edge, tick):
        self.last_tick = tick
        for pin, cb in zip(self.pins, self.callbacks):
            if pin == event:
                result = cb(edge, tick)
                if inspect.isawaitable(result):
                    await result

    def _register_callback(self, pin, cb):
        self.callbacks = self.callbacks + [cb]
        self.pins = self.pins + [pin]

    def monitor_pin(self, pin, cb, rising=True, falling=False, pullUp=False, pullDown=False, filterUs=0):
        raise RuntimeError("Not implemented")