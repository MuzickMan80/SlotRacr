from aiohttp import web
from aiohttp.web_request import Request
from racr.flags import Flags
from racr.track_manager import TrackManager
from racr.settings.track_settings import save_settings
from racr.settings.track_settings import track_settings
import jsons
import os

routes = web.RouteTableDef()

track: TrackManager = None

@routes.get('/settings')
async def get_settings(request):
    return web.json_response(jsons.dump(track_settings))
        
@routes.get('/settings/{group}')
async def get_setting_group(request):
    group=request.match_info['group']
    return web.json_response(jsons.dump(track_settings[group]))
  
@routes.get('/settings/{group}/{setting}')
async def get_setting(request):
    group=request.match_info['group']
    setting=request.match_info['setting']
    return web.json_response(jsons.dump(track_settings[group][setting]))

@routes.get('/settings/{group}/{setting}/{property}')
async def get_setting_property(request):
    group=request.match_info['group']
    setting=request.match_info['setting']
    property=request.match_info['property']
    return web.json_response(jsons.dump(track_settings[group][setting].__dict__[property]))

@routes.put('/settings/{group}/{setting}/value')
async def put_setting_property(request:Request):
    group=request.match_info['group']
    setting=request.match_info['setting']
    s=track_settings[group][setting]
    await s.set_value(await request.json())
    save_settings()
    return web.json_response(jsons.dump(s.value))

@routes.put('/race/state')
async def put_state(request:Request):
    await track.set_web_state(Flags.parse(request.json()))
    return web.json_response(jsons.dump(track.web_state))

@routes.get('/race/state')
async def get_state(request:Request):
    return web.json_response(jsons.dump(track.web_state))

@routes.put('/race/{lane}/accident')
async def put_state(request:Request):
    lane=request.match_info['lane']
    await track.set_web_state(Flags.parse(request.json()))
    return web.json_response(jsons.dump(track.web_state))

@routes.get('/race/{lane}/accident')
async def get_state(request:Request):
    lane=request.match_info['lane']
    return web.json_response(jsons.dump(track.web_state))

@routes.route('*', '/{tail:.*}')
async def root_handler(request:Request):
    root = 'SlotRacr/web_frontend/dist/FrontEnd'
    path = f'{root}/{request.path}'
    if (os.path.isfile(path)):
        return web.FileResponse(path)
    else:
        return web.HTTPFound('/index.html')
