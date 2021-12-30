from racr.io.io_manager import IoManager, SECONDS
from .pit_button import PitButton
import random
import asyncio

class Pit:
    def __init__(self,io_manager:IoManager,lane,cb) -> None:
        self.button = PitButton(io_manager,lane,self.pit_button_pressed,self.pit_button_down)
        self.io_manager = io_manager
        self.reset()
        self.cb = cb

    def reset(self):
        self.laps_driven=0
        self.low_fuel=False
        self.out_of_fuel=False
        self.in_pits=False
        self.pitting=False
        self.pit_this_lap=False
        self.pit_progress=0
        self.lap_time=0

    def pit_button_pressed(self):
        pass

    async def pit_button_down(self,down):
        if not self.pit_this_lap:
            micros_since_lap = self.io_manager.tick_diff_micros(self.lap_time, self.io_manager.last_tick)
            pit_this_lap = micros_since_lap < 2 * SECONDS and down
            if pit_this_lap != self.pit_this_lap:
                self.pit_this_lap = pit_this_lap
                await self.cb()
        elif self.pitting != down:
            self.pitting = down
            await self.cb()


    def get_indicator(self) -> str:
        if self.in_pits:
            return str(self.pit_progress)
        if self.pitting:
            return "slow"
        if self.pit_this_lap:
            return "pit_rq"
        if self.out_of_fuel:
            return "no_gas"
        if self.low_fuel:
            return "lo_gas"
        return "go"

    async def lap(self):
        self.lap_time = self.io_manager.last_tick

        if self.pitting:
            self.in_pits = True
            asyncio.create_task(self._pitting())

        self.pit_this_lap = False
        self.laps_driven = self.laps_driven+1
        if self.laps_driven == 45:
            self.low_fuel = True
            asyncio.create_task(self._running_out_of_fuel())

    async def _running_out_of_fuel(self):
        probability = 0
        while self.low_fuel:
            out_of_fuel = random.randrange(100) < probability
            if out_of_fuel != self.out_of_fuel:
                self.out_of_fuel = out_of_fuel
                await self.cb()

            probability = probability + 5
            wait_time = random.randrange(500,1000)
            await asyncio.sleep(wait_time/1000)

    async def _pitting(self):
        while self.pit_progress < 3:
            wait_time = random.randrange(2000,4000)
            await asyncio.sleep(wait_time/1000)
            self.pit_progress = self.pit_progress + 1
            await self.cb()
        self.reset()
        await self.cb()

    def throttle(self, max_throttle=100):
        if self.in_pits:
            return 0
        if self.out_of_fuel or self.pitting:
            return min(max_throttle, 50)
        return max_throttle
        