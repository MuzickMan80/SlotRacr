from util.observable import Observable
from .lane_timer import LaneTimer
from .pit import Pit
from .lane_state_reporter import LaneStateReporter
from .speed_control import SpeedControl
from .fuel import Fuel
from racr.flags import Flags

class Lane(Observable):
    def __init__(self, io_manager, lane, observer):
        super().__init__(observer)
        self.name = ''
        self.lane = lane
        self.timer = LaneTimer(io_manager, lane, self.lane_updated)
        self.pit = Pit(io_manager, lane, self.pit_updated)
        self.speed = SpeedControl(io_manager, lane)
        self.fuel = Fuel(self.fuel_updated)
        self.flag = Flags.green

    async def reset(self):
        self.timer.reset()
        self.pit.reset()
        self.fuel.reset()

    async def lane_updated(self):
        await self.fuel.update_lane_status(self.timer.laps)
        await self.pit.lap()
        self.update_throttle()
        await self.notify_observer_async()

    async def pit_updated(self):
        await self.fuel.update_pit_status(self.pit.in_pits)
        self.update_throttle()
        await self.notify_observer_async()

    async def fuel_updated(self):
        self.pit.out_of_fuel = self.fuel.out_of_fuel
        self.update_throttle()
        await self.notify_observer_async()
    
    async def set_current_flag(self, flag: Flags):
        self.flag = flag
        self.update_throttle()

    def update_throttle(self):
        stop = self.pit.in_pits or self.flag == Flags.red
        slow = self.pit.pitting or self.pit.penalty or self.flag == Flags.yellow
        self.speed.set_speed(slow, stop, self.fuel.out_of_fuel)
    
    def state(self):
        reporter = LaneStateReporter(self, self.timer, self.pit, self.fuel)
        return reporter.report_state()