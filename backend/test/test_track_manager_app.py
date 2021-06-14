import asyncio
from io_manager import SECONDS
from test.fake_io_manager import FakeIoManager
from app import TrackManagerApp
import json
from unittest.mock import AsyncMock
import pytest
import socketio

@pytest.fixture
async def backend_server():
    io = FakeIoManager()
    track = TrackManagerApp(io,3,[4,5,6,7,8])
    await track.start()
    yield track
    await track.stop()

class TrackClient(socketio.AsyncClientNamespace):
    def __init__(self):
        super().__init__()
        self.sio = socketio.AsyncClient(logger=True)
        self.sio.register_namespace(self)
        self.update_cb = AsyncMock()

    async def connect(self):
        await self.sio.connect('http://localhost:5000')

    async def disconnect(self):
        await self.sio.disconnect()

    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    async def on_update(self, data):
        print("Got update")
        await self.update_cb(data)

    def last_update(self):
        self.update_cb.assert_called()
        return json.loads(self.update_cb.call_args[0][0])

    async def request_update(self):
        await self.emit('update')

    async def simulate_activity(self, on, rate):
        await self.emit('simulate_activity', { 'enable': on, 'rate': rate })

@pytest.fixture
async def backend_client(backend_server):
    trackClient = TrackClient()
    await trackClient.connect()
    await asyncio.sleep(.1)
    yield trackClient
    await trackClient.disconnect()

@pytest.mark.asyncio 
async def test_update_request(backend_client):
    # Request an update from the server
    await backend_client.request_update()
    await asyncio.sleep(.1)
    backend_client.update_cb.assert_called_once()
    assert backend_client.last_update()[1]["started"] == False

@pytest.mark.asyncio 
async def test_lane_activity_triggers_update(backend_client, backend_server):
    # Start a lane, and ensure we get an automatic update
    await backend_server.track.io_manager.invoke_callback(5,1*SECONDS)
    await asyncio.sleep(.1)
    backend_client.update_cb.assert_called_once()
    assert backend_client.last_update()[1]["started"] == True

@pytest.mark.asyncio
async def test_simulate_activity(backend_client: TrackClient):
    await backend_client.simulate_activity(True, 0.01)
    await asyncio.sleep(1)
    await backend_client.simulate_activity(False, 0.05)
    await asyncio.sleep(0.1)
    assert backend_client.update_cb.call_count > 3
    backend_client.update_cb.reset_mock()
    await asyncio.sleep(0.5)
    assert backend_client.update_cb.call_count == 0
