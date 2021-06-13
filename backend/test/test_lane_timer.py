from ..io_manager import SECONDS
from .fake_io_manager import FakeIoManager
from ..lane_timer import LaneTimer
import unittest
from unittest.mock import AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio 
async def test_lane_timer():
    io = FakeIoManager()
    cb = MagicMock()
    lane = LaneTimer(io, lane=1, pin=5, cb=cb)
    
    await io.invoke_callback(5,5*SECONDS)
    assert lane.laps == 0
    assert cb.call_count == 1

    await io.invoke_callback(5,13*SECONDS)
    assert lane.laps == 1
    assert cb.call_count == 2
    assert lane.last == 8 * SECONDS
    assert lane.best == 8 * SECONDS

    await io.invoke_callback(5,13.1*SECONDS)
    assert lane.laps == 1
    assert lane.skippedTriggers == 1
    assert cb.call_count == 2

    await io.invoke_callback(5, 27*SECONDS)
    assert lane.last == 14 * SECONDS
    assert lane.best == 8 * SECONDS

    state = lane.state()
    assert state["lane"] == 1
    assert state["laps"] == 2
    assert state["last"] == 14
    assert state["best"] == 8
    assert state["pos"] == 0
    assert state["started"] == True

    lane.reset()
    state = lane.state()
    assert state["lane"] == 1
    assert state["laps"] == 0
    assert state["last"] == None
    assert state["best"] == None
    assert state["pos"] == 0
    assert state["started"] == False