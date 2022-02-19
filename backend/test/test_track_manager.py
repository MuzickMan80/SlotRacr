from racr.io.fake_io_manager import FakeIoManager
from racr.io.io_manager import SECONDS
from racr.track_manager import TrackManager
from unittest.mock import AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio 
async def test_track_manager():
    io = FakeIoManager()
    cb = MagicMock()
    
    track = TrackManager(io,cb)
    
    await io.invoke_lane_pin_callback(0, 2*SECONDS)
    assert cb.call_count == 1
    assert track.lanes[0].timer.started

    await io.invoke_lane_pin_callback(0, 7*SECONDS)
    assert cb.call_count == 2

    await io.invoke_callback(io.get_reset_pin(), 12*SECONDS, False)
    assert cb.call_count == 3
    assert not track.lanes[0].timer.started
    
@pytest.mark.asyncio
async def test_async_track_manager():
    io = FakeIoManager()
    cb = AsyncMock()
    track = TrackManager(io,cb)
    
    await io.invoke_callback(io.get_lane_pin(0), 2*SECONDS)
    assert cb.call_count == 1