import asyncio
from racr.io.io_manager import SECONDS
from racr.io.fake_io_manager import FakeIoManager
from aiohttp.test_utils import TestClient
from app_server import TrackManagerApp
import json
from unittest.mock import AsyncMock
import pytest
import socketio

@pytest.fixture
async def loop():
    loop = asyncio.get_event_loop()
    yield loop
    
@pytest.fixture
async def backend_server(loop):
    io = FakeIoManager()
    track = TrackManagerApp(io)
    await track.start()
    yield track
    await track.stop()

@pytest.fixture
async def backend_rest_client(aiohttp_client,backend_server: TrackManagerApp):
    yield await aiohttp_client(backend_server.webapp)
    
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
        await self.sio.wait()

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

async def test_update_request(backend_client):
    # Request an update from the server
    await backend_client.request_update()
    await asyncio.sleep(.1)
    backend_client.update_cb.assert_called_once()
    assert backend_client.last_update()["lanes"][1]["started"] == False

async def test_lane_activity_triggers_update(backend_client, backend_server):
    # Start a lane, and ensure we get an automatic update
    pin = backend_server.track.io_manager.get_lane_pin(1)
    await backend_server.track.io_manager.invoke_callback(pin,1*SECONDS,True)
    await asyncio.sleep(.1)
    backend_client.update_cb.assert_called_once()
    assert backend_client.last_update()["lanes"][1]["started"] == True

async def test_simulate_activity(backend_client: TrackClient):
    await backend_client.simulate_activity(True, 0.01)
    await asyncio.sleep(1)
    await backend_client.simulate_activity(False, 0.05)
    await asyncio.sleep(0.1)
    assert backend_client.update_cb.call_count > 3
    backend_client.update_cb.reset_mock()
    await asyncio.sleep(0.5)
    assert backend_client.update_cb.call_count == 0

async def test_track_getsettings(backend_rest_client):
    response = await backend_rest_client.get('/settings')
    assert(response.status == 200)
    settings = await response.json()
    assert(settings["race"]["enable_pitting"])

async def test_track_getracesettings(backend_rest_client):
    response = await backend_rest_client.get('/settings/race')
    assert(response.status == 200)
    settings = await response.json()
    assert(settings["enable_pitting"])

async def test_track_get_single_setting(backend_rest_client):
    response = await backend_rest_client.get('/settings/race/enable_pitting')
    assert(response.status == 200)
    settings = await response.json()
    assert(isinstance(settings['value'], bool))

async def test_track_get_single_setting_value(backend_rest_client):
    response = await backend_rest_client.get('/settings/race/enable_pitting/value')
    assert(response.status == 200)
    settings = await response.json()
    assert(isinstance(settings, bool))

async def test_track_put_single_setting_value(backend_rest_client:TestClient):
    response = await backend_rest_client.put('/settings/race/enable_pitting/value',json=True)
    assert(response.status == 200)
    settings = await response.json()
    assert(settings == True)
    response = await backend_rest_client.put('/settings/race/enable_pitting/value',json=False)
    assert(response.status == 200)
    settings = await response.json()
    assert(settings == False)
