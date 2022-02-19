
import asyncio
import random
from racr.io.io_manager import IoManager, SECONDS
from racr.flags import Flags

class RaceSimulator:
    def __init__(self, io_manager: IoManager, lanes):
        self.io_manager = io_manager
        self.lanes = lanes
        self.simulator = None
        self.enabled = False

    async def enable_activity_simulator(self, enable : bool, rate : float):
        if self.simulator:
            self.enabled = False
            await self.simulator
        self.enabled = enable
        if enable:
            loop = asyncio.get_event_loop()
            self.simulator = loop.create_task(self._simulate_activity(rate))

    async def _simulate_activity(self, rate: float):
        tick = self.io_manager.last_tick
        count = 0
        while self.enabled:
            lane = random.choice(self.lanes)
            try:
                await lane.timer.lap(True, tick)
            except Exception as ex:
                print(f'Error simulating step: {ex}')
            await asyncio.sleep(rate)
            tick = tick + rate * SECONDS

            count = count + 1
            if count == 10:
                count = 0
                state = random.uniform(0,1)<.25
                button = 8+int(random.uniform(0,1)<0.5)
                await self.io_manager.lane_controller.handle_button(button, state)
