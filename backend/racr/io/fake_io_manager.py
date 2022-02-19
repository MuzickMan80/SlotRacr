import asyncio
from racr.lane_controller.lane_controller import LaneController
from racr.io.io_manager import IoManager
from unittest.mock import MagicMock

reset_pin = 1
lane_pins = [2,3,4,5,6,7,8,9]
pit_pins = [10,11,12,13,14,15,16,17]

class FakeIoManager(IoManager):
    def __init__(self, async_loop=None):
        if not async_loop:
            async_loop = asyncio.get_event_loop()
        IoManager.__init__(self, async_loop)
        self.lane_controller=MagicMock(spec=LaneController)

    def get_lane_pin(self, lane) -> int:
        return lane_pins[lane]

    def get_reset_pin(self) -> int:
        return reset_pin

    def get_pit_pin(self, lane) -> int:
        return pit_pins[lane]

    async def invoke_lane_pin_callback(self, lane, tick, edge=False):
        await self.invoke_callback(self.get_lane_pin(lane), tick, edge)

    async def invoke_callback(self, pin, tick, edge=False):
        self._io_update(pin, edge, tick)
        await asyncio.sleep(0.001)

    def monitor_pin(self, pin, cb, rising=True, falling=False, pullUp=False, pullDown=True, filterUs=0):
        self._register_callback(pin, cb)
