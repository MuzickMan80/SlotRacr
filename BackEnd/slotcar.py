#!/usr/bin/env python3

import pigpio
import time
import socketio
import json
import asyncio
import sys
from aiohttp import web

if len(sys.argv) >= 2:
    '''/*'169.254.154.109'*/'''
    pi = pigpio.pi(sys.argv[1])
else:
    pi = pigpio.pi()

if not pi.connected:
    print('Failed to connect to pigpio server')
    exit()

print('gpio connection succeeded')

class LaneTimer(object):
    def __init__(self, lane):
        self.lane = lane
        self.reset()
    def lap(self, tick):
        if self.started:
            diff = pigpio.tickDiff(self.lapStartTime, tick)
            if diff < 500000:
                return False
            self.last = diff
            self.laps = self.laps + 1
            if self.best == None or self.last < self.best:
                self.best = self.last
        self.lapStartTime = tick
        self.started = True
        print(self.last, self.best)
        return True
    def reset(self):
        self.best = None
        self.last = None
        self.lapStartTime = 0
        self.started = False
        self.laps = 0
        self.pos = 0
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

lanes = [LaneTimer(1), LaneTimer(2), LaneTimer(3), LaneTimer(4)]

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def emitLaneDump():
    lane_dump = json.dumps(list(
        map(lambda l: l.state(), lanes)))
    print(lane_dump)
    await sio.emit('update', lane_dump)

@sio.event
async def connect(sid, environ):
    print('onConnect')
    await emitLaneDump()

@sio.event
async def message(sid, environ):
    print('message')
    await emitLaneDump()

def updateLanePos(tick):
    lane_pos = lanes.copy()
    lane_pos.sort(key=lambda l: (-l.laps, -pigpio.tickDiff(l.lapStartTime, tick)))
    for i in range(0,4):
        if lane_pos[i].laps > 0:
            lane_pos[i].pos = i+1
        else:
            lane_pos[i].pos = len(lanes)

pins = [5,6,13,19,26]

async def io_update(event, tick):
    idx = pins.index(event)
    if idx == 0:
        for lane in lanes:
            lane.reset()
        await emitLaneDump()
    else:
        if lanes[idx-1].lap(tick):
            updateLanePos(tick)
            await emitLaneDump()

loop = asyncio.get_event_loop()

def cbf(event, level, tick):
    asyncio.run_coroutine_threadsafe(io_update(event, tick),loop)

for pin in pins:
    pi.set_mode(pin, pigpio.INPUT)
    pi.set_pull_up_down(pin, pigpio.PUD_UP)
    print(pin, pi.read(pin))
    pi.callback(pin, 1, cbf)

if __name__ == '__main__':
    web.run_app(app, port=5000)
