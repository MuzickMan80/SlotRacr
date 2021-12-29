from racr.io.fake_io_manager import FakeIoManager
from racr.io.io_manager import SECONDS
from racr.track_manager import TrackManager
from unittest.mock import AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio 
async def test_track_manager():
    io = FakeIoManager()
    cb = MagicMock()
    track = TrackManager(io,3,[4,5,6,7,8],cb)
    
    await io.invoke_callback(4, 2*SECONDS)
    assert cb.call_count == 1
    assert track.lanes[0].started

    await io.invoke_callback(4, 5*SECONDS)
    assert cb.call_count == 2

    await io.invoke_callback(3, 7*SECONDS)
    assert cb.call_count == 3
    assert not track.lanes[0].started
    
@pytest.mark.asyncio
async def test_async_track_manager():
    io = FakeIoManager()
    cb = AsyncMock()
    track = TrackManager(io,3,[4,5,6,7,8],cb)
    
    await io.invoke_callback(4, 2*SECONDS)
    assert cb.call_count == 1