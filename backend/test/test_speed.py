from racr.io.io_manager import SECONDS
from racr.io.fake_io_manager import FakeIoManager
from racr.lane.lane import Lane
from unittest.mock import MagicMock, AsyncMock
from racr.lane.speed_control import SpeedControl
import pytest

@pytest.mark.asyncio 
async def test_damage_penalty():
    io = FakeIoManager()
    laneIdx = 0
    speed = SpeedControl(io, laneIdx)

    speed.set_max_speed(60)
    speed.set_speed(False, False, False, 0)

    assert speed.speed == 60

    speed.set_speed(False, False, False, 1)

    assert speed.speed == 30

    speed.set_speed(False, False, False, 2)

    assert speed.speed == 21

    speed.set_speed(False, False, False, 3)

    assert speed.speed == pytest.approx(16.2)

    speed.set_speed(False, False, False, 4)

    assert speed.speed == pytest.approx(11.4)
