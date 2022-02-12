from aiohttp import web
from aiohttp.web_request import Request
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
    if property=='value':
        return web.json_response(jsons.dump(track_settings[group][setting].value))
    else:
        return web.json_response(jsons.dump(track_settings[group][setting].__dict__[property]))

@routes.put('/settings/{group}/{setting}/value')
async def put_setting_property(request:Request):
    group=request.match_info['group']
    setting=request.match_info['setting']
    s=track_settings[group][setting]
    s.value = await request.json()
    save_settings()
    return web.json_response(jsons.dump(s.value))

@routes.route('*', '/{tail:.*}')
async def root_handler(request:Request):
    root = 'SlotRacr/web_frontend/dist/FrontEnd'
    path = f'{root}/{request.path}'
    if (os.path.isfile(path)):
        return web.FileResponse(path)
    else:
        return web.HTTPFound('/index.html')
