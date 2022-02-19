from racr.race.race_simulator import RaceSimulator
from racr.flags import Flags
from util.observable import Observable
from .io.io_manager import IoManager, SECONDS
from .lane.lane import Lane

class TrackManager(Observable):
    def __init__(self,io_manager: IoManager,observer):
        super().__init__(observer)
        io_manager.monitor_reset_pin(self.reset_handler)
        io_manager.monitor_warn_pin(self.warn_handler)
        io_manager.monitor_stop_pin(self.stop_handler)
        self.io_manager = io_manager
        self.lanes: list[Lane] = []
        self.num_laps = 100
        self.current_lap = 0
        self.flag = Flags.green
        self.warn_button = False
        self.stop_button = False
        for lane in range(8):
            self.lanes = self.lanes + [Lane(io_manager,lane,self.lap_handler)]

        self.simulator = RaceSimulator(io_manager, self.lanes)
        
    async def reset_handler(self):
        for lane in self.lanes:
            await lane.reset()
        await self.notify_observer_async()

    async def warn_handler(self, down):
        self.warn_button = down
        await self.calculate_current_flag()

    async def stop_handler(self, down):
        self.stop_button = down
        await self.calculate_current_flag()

    async def calculate_current_flag(self):
        flag = Flags.green
        if self.stop_button:
            flag = Flags.red
        elif self.current_lap >= self.num_laps:
            flag = Flags.checkered
        elif self.warn_button:
            flag = Flags.yellow
        elif self.current_lap == self.num_laps-1:
            flag = Flags.white

        if flag != self.flag:
            for lane in self.lanes:
                await lane.set_current_flag(flag)
            self.flag=flag
            await self.notify_observer_async()

    async def lap_handler(self):
        tick = self.io_manager.last_tick
        lane_pos = self.lanes.copy()
        lane_pos.sort(key=lambda l: (-l.timer.laps, self.io_manager.tick_diff_micros(l.timer.lapStartTime, tick)))
        i = 1
        for l in lane_pos:
            if l.timer.laps > 0:
                l.pos = i
            else:
                l.pos = len(self.lanes)
            i = 1 + i
        self.current_lap = max(map(lambda l: l.timer.laps, self.lanes))
        await self.calculate_current_flag()
        await self.notify_observer_async()

    def enable_activity_simulator(self, enable : bool, rate : float):
        self.simulator.enable_activity_simulator(enable, rate)
