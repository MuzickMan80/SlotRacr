from .pit import Pit
from racr.io.io_manager import IoManager

class LaneTimer(object):
    def __init__(self, io_manager: IoManager, lane, cb):
        self.lane = lane
        self.io_manager = io_manager
        self.observer = cb
        self.minimum_lap_time = 3.5
        self.reset()
        io_manager.monitor_lane_pin(lane, self.lap)
    
    async def lap(self, event, tick):
        if self.started:
            diff = self.io_manager.tick_diff_micros(self.lapStartTime, tick)
            if diff < self.minimum_lap_time * 1e6:
                self.skippedTriggers = self.skippedTriggers + 1
                return
            self.last = diff
            self.laps = self.laps + 1
            if self.best == None or self.last < self.best:
                self.best = self.last
        self.lapStartTime = tick
        self.started = True
        await self.observer()

    def reset(self):
        self.best = None
        self.last = None
        self.lapStartTime = 0
        self.started = False
        self.laps = 0
        self.pos = 0
        self.skippedTriggers = 0
        return self
