from racr.race.race_simulator import RaceSimulator
from util.observable import Observable
from .io.io_manager import IoManager, SECONDS
from .lane.lane_timer import LaneTimer
from .io.button import Button

class TrackManager(Observable):
    def __init__(self,io_manager,observer):
        super().__init__(observer)
        self.resetter = Button(io_manager, io_manager.get_reset_pin(), self.reset_handler)
        self.io_manager: IoManager = io_manager
        self.lanes: list[LaneTimer] = []
        for lane in range(8):
            pin = io_manager.get_lane_pin(lane)
            self.lanes = self.lanes + [LaneTimer(io_manager,lane+1,pin,self.lap_handler)]

        self.simulator = RaceSimulator(io_manager, self.lanes)
        
    async def reset_handler(self):
        for lane in self.lanes:
            lane.reset()
        await self.notify_observer()

    async def lap_handler(self):
        tick = self.io_manager.last_tick
        lane_pos = self.lanes.copy()
        lane_pos.sort(key=lambda l: (-l.laps, self.io_manager.tick_diff_micros(l.lapStartTime, tick)))
        i = 1
        for l in lane_pos:
            if l.laps > 0:
                l.pos = i
            else:
                l.pos = len(self.lanes)
            i = 1 + i
        await self.notify_observer()

    def enable_activity_simulator(self, enable : bool, rate : float):
        self.simulator.enable_activity_simulator(enable, rate)
