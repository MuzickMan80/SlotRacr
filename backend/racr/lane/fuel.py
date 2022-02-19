from util.observable import Observable
import random
import asyncio

class Fuel(Observable):
    def __init__(self, observer):
        super().__init__(observer)
        self.laps_until_low = 45
        self.max_laps_after_low = 15
        self.mean_laps_after_low = 10
        self.laps_after_low = 10
        self.laps_driven = 0
        self.last_pit_lap = 0
        self.last_lap = 0
        self.low_fuel=False
        self.out_of_fuel=False

    async def update_lane_status(self, laps):
        self.last_lap = laps
        self.laps_driven = laps - self.last_pit_lap
        if self.laps_driven == self.laps_until_low:
            self.low_fuel = True
            asyncio.create_task(self._running_out_of_fuel())

    async def update_pit_status(self, in_pits):
        if in_pits:
            self.last_pit_lap - self.last_lap
            self.low_fuel = False
            self.out_of_fuel = False
            self.laps_driven = 0
            await self.notify_observer_async()
    
    async def _running_out_of_fuel(self):
        probability = 0
        while self.low_fuel:
            out_of_fuel = random.randrange(100) < probability
            if out_of_fuel and not self.out_of_fuel:
                self.out_of_fuel = out_of_fuel
                await self.notify_observer_async()
                return

            probability = probability + 5
            wait_time = random.randrange(500,1000)
            await asyncio.sleep(wait_time/1000)
