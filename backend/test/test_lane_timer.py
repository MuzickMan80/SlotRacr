from racr.io.io_manager import SECONDS
from racr.io.fake_io_manager import FakeIoManager
from racr.lane.lane import Lane
from unittest.mock import MagicMock, AsyncMock
import pytest

@pytest.mark.asyncio 
async def test_lane_timer():
    io = FakeIoManager()
    cb = AsyncMock()
    laneIdx=0
    lane = Lane(io, laneIdx, cb)
    
    await io.invoke_lane_pin_callback(laneIdx,5*SECONDS)
    assert lane.timer.laps == 0
    assert cb.call_count == 1

    await io.invoke_lane_pin_callback(laneIdx,13*SECONDS)
    assert lane.timer.laps == 1
    assert cb.call_count == 2
    assert lane.timer.last == 8 * SECONDS
    assert lane.timer.best == 8 * SECONDS

    await io.invoke_lane_pin_callback(laneIdx,13.1*SECONDS)
    assert lane.timer.laps == 1
    assert lane.timer.skippedTriggers == 1
    assert cb.call_count == 2

    await io.invoke_lane_pin_callback(laneIdx, 27*SECONDS)
    assert lane.timer.last == 14 * SECONDS
    assert lane.timer.best == 8 * SECONDS

    state = lane.state()
    assert state["lane"] == 1
    assert state["laps"] == 2
    assert state["last"] == 14
    assert state["best"] == 8
    assert state["pos"] == 0
    assert state["started"] == True

    await lane.reset()
    state = lane.state()
    assert state["lane"] == 1
    assert state["laps"] == 0
    assert state["last"] == None
    assert state["best"] == None
    assert state["pos"] == 0
    assert state["started"] == False