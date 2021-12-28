
import asyncio
import random
from racr.io.io_manager import IoManager, SECONDS

class RaceSimulator:
    def __init__(self, io_manager: IoManager, lanes):
        self.io_manager = io_manager
        self.lanes = lanes
        self.simulator = None

    def enable_activity_simulator(self, enable : bool, rate : float):
        if self.simulator:
            self.simulator.cancel()
            self.simulator = None
        if enable:
            self.simulator = asyncio.create_task(self._simulate_activity(rate))

    async def _simulate_activity(self, rate: float):
        tick = self.io_manager.last_tick
        while True:
            lane = random.choice(self.lanes)
            await lane.lap(True, tick)
            await asyncio.sleep(rate)
            tick = tick + rate * SECONDS