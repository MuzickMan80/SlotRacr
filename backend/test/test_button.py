
from test.fake_io_manager import FakeIoManager
from racr.io.button import Button
from unittest.mock import AsyncMock, MagicMock
import pytest

@pytest.mark.asyncio 
async def test_async_button():
    io = FakeIoManager()
    cb = AsyncMock()
    button = Button(io, 5, cb)
    await io.invoke_callback(5,500)
    cb.assert_called_once()

    await io.invoke_callback(5,1000)
    assert cb.call_count == 2

    #Ensure the wrong pin number doesn't invoke the button
    await io.invoke_callback(6,1500)
    assert cb.call_count == 2

@pytest.mark.asyncio 
async def test_button():
    io = FakeIoManager()
    cb = MagicMock()
    button = Button(io, 5, cb)
    await io.invoke_callback(5,500)
    cb.assert_called_once()

    await io.invoke_callback(5,1000)
    assert cb.call_count == 2

    #Ensure the wrong pin number doesn't invoke the button
    await io.invoke_callback(6,1500)
    assert cb.call_count == 2
