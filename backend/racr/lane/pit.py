from racr.io.io_manager import IoManager, SECONDS
from util.observable import Observable
import random
import asyncio

class Pit(Observable):
    def __init__(self,io_manager:IoManager,lane,observer) -> None:
        super().__init__(observer)
        io_manager.lane_controller.monitor_button(lane,self.pit_button_down)
        self.io_manager = io_manager
        self.lane_controller = io_manager.lane_controller
        self.lane = lane
        self.require_crew_alert = True
        self.reset()

    def reset(self):
        self.in_pits=False
        self.pitting=False
        self.pit_this_lap=False
        self.penalty=False
        self.micros_pitting=0
        self.pit_progress=0
        self.lap_time=0
        self.pit_start_time=0
        self.out_of_fuel=False

    async def pit_button_down(self,down):
        if self.require_crew_alert and not self.out_of_fuel and not self.pit_this_lap:
            micros_since_lap = self.io_manager.tick_diff_micros(self.lap_time, self.io_manager.last_tick)
            pit_this_lap = micros_since_lap < 2 * SECONDS and down
            if pit_this_lap != self.pit_this_lap:
                self.pit_this_lap = pit_this_lap
                await self.notify_observer_async()
        elif self.pitting != down:
            self.pitting = down
            if self.pitting:
                self.pit_start_time = self.io_manager.last_tick
            await self.notify_observer_async()

    async def lap(self):
        self.lap_time = self.io_manager.last_tick

        if self.pitting:
            self.in_pits = True
            asyncio.create_task(self._pitting())

        self.pit_this_lap = False

    def _normalize(_, val, zero_val, one_val):
        val_range = one_val - zero_val
        normalized_val = (val - zero_val) / val_range
        return min(1, max(0, normalized_val))

    async def _pitting(self):
        micros_pitting = self.io_manager.tick_diff_micros(self.pit_start_time, self.io_manager.last_tick)
        # Should be 0 if >1.5 seconds, or 100% if <1.0 seconds
        sure_penalty = 1 * SECONDS
        no_penalty = 1.5 * SECONDS
        penalty_prob = 100 * self._normalize(micros_pitting, zero_val=no_penalty, one_val=sure_penalty)
        
        penalty = random.randrange(100) <= penalty_prob
        self.penalty = penalty
        self.micros_pitting = micros_pitting
        await self.notify_observer_async()

        pit_time = random.triangular(10,40,13)
        self.pit_progress = 0
        sleep_time = 0.2
        while self.in_pits and self.pit_progress < pit_time:
            self.pit_progress = self.pit_progress + sleep_time
            await self.notify_observer_async()
            await asyncio.sleep(sleep_time)

        if self.in_pits:
            self.reset()
            self.penalty = penalty
            await self.notify_observer_async()