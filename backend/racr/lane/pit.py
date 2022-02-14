from racr.io.io_manager import IoManager, SECONDS
from racr.lane_controller.lane_controller import LaneController, Button
import random
import asyncio

class Pit:
    def __init__(self,io_manager:IoManager,lane,cb) -> None:
        self.button = Button(io_manager.lane_controller, lane, down_handler=self.pit_button_down)
        self.io_manager = io_manager
        self.lane_controller = io_manager.lane_controller
        self.lane = lane
        self.require_crew_alert = True
        self.laps_until_out=45
        self.reset()
        self.cb = cb

    def reset(self):
        self.laps_driven=0
        self.low_fuel=False
        self.out_of_fuel=False
        self.in_pits=False
        self.pitting=False
        self.pit_this_lap=False
        self.penalty=False
        self.micros_pitting=0
        self.pit_progress=0
        self.lap_time=0
        self.pit_start_time=0
        self.update_throttle()

    def light_pit_button(self,on):
        self.lane_controller.set_light(self.lane,on)

    def set_lane_speed(self,speed):
        self.lane_controller.set_lane(self.lane,speed)

    def set_lane_oog(self):
        self.lane_controller.set_oog(self.lane, 35, 77, 0)

    def pit_button_pressed(self):
        pass

    async def pit_button_down(self,down):
        self.light_pit_button(down)
        if self.require_crew_alert and not self.out_of_fuel and not self.pit_this_lap:
            micros_since_lap = self.io_manager.tick_diff_micros(self.lap_time, self.io_manager.last_tick)
            pit_this_lap = micros_since_lap < 2 * SECONDS and down
            if pit_this_lap != self.pit_this_lap:
                self.pit_this_lap = pit_this_lap
                await self.cb()
        elif self.pitting != down:
            self.pitting = down
            if self.pitting:
                self.pit_start_time = self.io_manager.last_tick
            await self.cb()

    def get_indicator(self) -> str:
        if self.in_pits:
            return str(self.pit_progress)
        if self.pitting:
            return "slo"
        if self.pit_this_lap:
            return "pit"
        if self.out_of_fuel:
            return "out"
        if self.low_fuel:
            return "lgas"
        if self.penalty:
            return "plty"
        return "go"

    async def lap(self):
        self.lap_time = self.io_manager.last_tick

        if self.pitting:
            self.in_pits = True
            asyncio.create_task(self._pitting())

        self.pit_this_lap = False
        self.laps_driven = self.laps_driven+1
        if self.laps_driven == self.laps_until_out:
            self.low_fuel = True
            asyncio.create_task(self._running_out_of_fuel())

    async def _running_out_of_fuel(self):
        probability = 0
        while self.low_fuel:
            out_of_fuel = random.randrange(100) < probability
            if out_of_fuel and not self.out_of_fuel:
                self.out_of_fuel = out_of_fuel
                self.update_throttle()
                await self.cb()
                return

            probability = probability + 5
            wait_time = random.randrange(500,1000)
            await asyncio.sleep(wait_time/1000)

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
        self.update_throttle()

        while True:
            wait_time = random.randrange(2000,4000)
            await asyncio.sleep(wait_time/1000)
            self.pit_progress = self.pit_progress + 1
            if self.pit_progress == 3:
                self.reset()
                self.penalty = penalty
                self.micros_pitting = micros_pitting
                await self.cb()
                break

            await self.cb()

    def update_throttle(self):
        throttle = 100
        if self.in_pits:
            self.set_lane_speed(0)
            throttle = 0
        elif self.out_of_fuel:
            throttle=min(throttle, 25)
            self.set_lane_oog()
        elif self.pitting or self.penalty:
            throttle=min(throttle, 50)
            self.set_lane_speed(throttle)
        else:
            self.set_lane_speed(throttle)

        self.throttle=throttle
        return throttle
        