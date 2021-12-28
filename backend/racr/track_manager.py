from backend.racr.race.race_simulator import RaceSimulator
from util.observable import Observable
from .io.io_manager import IoManager, SECONDS
from .lane.lane_timer import LaneTimer
from .io.button import Button

class TrackManager(Observable):
    def __init__(self,io_manager,reset_pin,lane_pins,observer):
        super().__init__(observer)
        self.resetter = Button(io_manager, reset_pin, self.reset_handler)
        self.io_manager: IoManager = io_manager
        self.lanes: list[LaneTimer] = []
        laneIdx = 1
        for pin in lane_pins:
            self.lanes = self.lanes + [LaneTimer(io_manager,laneIdx,pin,self.lap_handler)]
            laneIdx = laneIdx + 1

        self.simulator = RaceSimulator(io_manager, self.lanes)
        
    async def reset_handler(self):
        for lane in self.lanes:
            lane.reset()
        await self.notify_observer()

    async def lap_handler(self):
        tick = self.io_manager.last_tick
        lane_pos = self.lanes.copy()
        lane_pos.sort(key=lambda l: (-l.laps, self.io_manager.tick_diff(l.lapStartTime, tick)))
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
        