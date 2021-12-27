
class LaneTimer(object):
    def __init__(self, io_manager, lane, pin, cb):
        self.lane = lane
        self.io_manager = io_manager
        self.pin = pin
        self.on_lap = cb
        self.reset()
        io_manager.monitor_pin(pin, self.lap)
    
    async def lap(self, event, tick):
        if self.started:
            diff = self.io_manager.tick_diff(self.lapStartTime, tick)
            if diff < 500000:
                self.skippedTriggers = self.skippedTriggers + 1
                return
            self.last = diff
            self.laps = self.laps + 1
            if self.best == None or self.last < self.best:
                self.best = self.last
        self.lapStartTime = tick
        self.started = True
        await self.on_lap()

    def reset(self):
        self.best = None
        self.last = None
        self.lapStartTime = 0
        self.started = False
        self.laps = 0
        self.pos = 0
        self.skippedTriggers = 0
        return self
    def state(self):
        return {'lane': self.lane,
                'best': self.time_string(self.best),
                'last': self.time_string(self.last),
                'laps': self.laps,
                'pos': self.pos,
                'started': self.started}
    def time_string(self, time):
        s = 0
        if time:
            s = time / 1000000
            return round(s,3)
        else:
            return None
