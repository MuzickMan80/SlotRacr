from racr.io.fake_io_manager import FakeIoManager
from racr.io.io_manager import SECONDS
from racr.track_manager import TrackManager
from unittest.mock import AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio 
async def test_track_manager():
    io = FakeIoManager()
    cb = MagicMock()
    lc = MagicMock()
    track = TrackManager(io,lc,cb)
    
    await io.invoke_callback(io.get_lane_pin(0), 2*SECONDS)
    assert cb.call_count == 1
    assert track.lanes[0].started

    await io.invoke_callback(io.get_lane_pin(0), 5*SECONDS)
    assert cb.call_count == 2

    await io.invoke_callback(io.get_reset_pin(), 7*SECONDS, False)
    assert cb.call_count == 3
    assert not track.lanes[0].started
    
@pytest.mark.asyncio
async def test_async_track_manager():
    io = FakeIoManager()
    cb = AsyncMock()
    lc = MagicMock()
    track = TrackManager(io,lc,cb)
    
    await io.invoke_callback(io.get_lane_pin(0), 2*SECONDS)
    assert cb.call_count == 1