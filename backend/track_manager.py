from backend.io_manager import IoManager
from .lane_timer import LaneTimer
from .button import Button
from .io_manager import SECONDS
import inspect
import asyncio
import random

class TrackManager:
    def __init__(self,io_manager,reset_pin,lane_pins,observer):
        self.resetter = Button(io_manager, reset_pin, self.reset_handler)
        self.observer = observer
        self.io_manager: IoManager = io_manager
        self.lanes: list[LaneTimer] = []
        self.simulator = None
        laneIdx = 1
        for pin in lane_pins:
            self.lanes = self.lanes + [LaneTimer(io_manager,laneIdx,pin,self.lap_handler)]
            laneIdx = laneIdx + 1
        
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

    async def notify_observer(self):
        result = self.observer()
        if inspect.isawaitable(result):
            await result

    def enable_activity_simulator(self, enable : bool, rate : float):
        if self.simulator:
            self.simulator.cancel()

        if enable:
            self.simulator = asyncio.create_task(self._simulate_activity(rate))

    async def _simulate_activity(self, rate: float):
        tick = self.io_manager.last_tick
        while True:
            lane = random.choice(self.lanes)
            await lane.lap(True, tick)
            await asyncio.sleep(rate)
            tick = tick + rate * SECONDS