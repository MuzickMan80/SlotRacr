from util.observable import Observable
import random
import asyncio

class Fuel(Observable):
    def __init__(self, observer):
        super().__init__(observer)
        self.laps_until_low = 45
        self.max_laps_after_low = 15
        self.mean_laps_after_low = 10
        self.seconds_per_lap = 5.5
        self.reset()

    def reset(self):
        self._laps_after_low = 10
        self._laps_driven = 0
        self._last_pit_lap = 0
        self._last_lap = 0
        self.low_fuel=False
        self.out_of_fuel=False

    async def update_lane_status(self, laps):
        self._last_lap = laps
        self._laps_driven = laps - self._last_pit_lap
        if self._laps_driven == self.laps_until_low:
            self.low_fuel = True
            asyncio.create_task(self._running_out_of_fuel())

    async def update_pit_status(self, in_pits):
        if in_pits:
            self._last_pit_lap - self._last_lap
            self.low_fuel = False
            self.out_of_fuel = False
            self._laps_driven = 0
            await self.notify_observer_async()
    
    async def _running_out_of_fuel(self):
        laps_until_out = random.triangular(0, self.max_laps_after_low, self.mean_laps_after_low)
        seconds_until_out = laps_until_out * self.seconds_per_lap
        while seconds_until_out > 1 and self.low_fuel:
            await asyncio.sleep(1)
            seconds_until_out = seconds_until_out - 1
        
        if self.low_fuel:
            await asyncio.sleep(seconds_until_out)
            self.out_of_fuel = True
            await self.notify_observer_async()
            