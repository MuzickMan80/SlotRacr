import asyncio
import json
from unittest.mock import AsyncMock
import pytest
import socketio
from racr.io.fake_io_manager import FakeIoManager
from app_server import TrackManagerApp

@pytest.fixture
async def loop():
    loop = asyncio.get_event_loop()
    yield loop
    
@pytest.fixture
async def backend_server(loop):
    io = FakeIoManager()
    track = TrackManagerApp(io)
    track.track.simulator.disabled = True
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
        await self.sio.connect('http://localhost:80')

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