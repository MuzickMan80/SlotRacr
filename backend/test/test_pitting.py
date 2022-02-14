from racr.lane_controller.lane_controller import LaneController
from racr.io.io_manager import SECONDS
from racr.io.fake_io_manager import FakeIoManager
from racr.lane.lane_timer import LaneTimer
from unittest.mock import MagicMock, AsyncMock, patch
import pytest
import asyncio

sleep = asyncio.sleep

async def run_tasks(delay=0):
    await sleep(.001)

@pytest.mark.asyncio
@patch('asyncio.sleep',side_effect=run_tasks)
async def test_oog_sequence(mock_sleep):
    io = FakeIoManager()
    cb = AsyncMock()
    lc=io.lane_controller
    laneIdx = 0
    lane = LaneTimer(io, lane=laneIdx, cb=cb)
    lane.pit.laps_until_out = 3
    
    assert lc.set_lane.call_count == 2
    lc.set_lane.assert_called_with(0,100)

    # Lap
    for lap in range(3):
        await io.invoke_lane_pin_callback(laneIdx,lap * 5 * SECONDS)
        assert lane.laps == lap
        assert lane.pit.low_fuel == False
        assert lane.pit.out_of_fuel == False

    await io.invoke_lane_pin_callback(laneIdx,20*SECONDS)
    assert lane.laps == 3
    assert lane.pit.low_fuel
    assert not lane.pit.out_of_fuel

    assert lc.set_lane.call_count == 2
    assert lc.set_oog.call_count == 0

    mock_sleep.reset_mock()
    for _ in range(20):
        await sleep(.001)
        if lane.pit.out_of_fuel:
            break

    assert lane.pit.out_of_fuel
    assert lc.set_lane.call_count == 2
    assert lc.set_oog.call_count == 1
    lc.set_oog.assert_called_with(0,35,77,0)

    # Ensure we can pit
    assert not lane.pit.in_pits
    pit_cb = lc.monitor_button.call_args.args[1]
    await pit_cb(True)
    await io.invoke_lane_pin_callback(laneIdx,30*SECONDS)
    await sleep(.001)
    assert lane.pit.in_pits
    
    assert lc.set_lane.call_count == 3
    assert lc.set_oog.call_count == 1
    lc.set_lane.assert_called_with(0,0)

    for _ in range(20):
        await sleep(.001)
        if not lane.pit.in_pits:
            break
    assert not lane.pit.in_pits
    assert not lane.pit.pitting
    assert lane.pit.laps_driven == 0
    assert lc.set_lane.call_count == 4
    assert lc.set_oog.call_count == 1
    lc.set_lane.assert_called_with(0,100)