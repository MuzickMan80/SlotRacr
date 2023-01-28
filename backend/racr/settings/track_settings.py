from typing import List
from racr.track_manager import TrackManager
from .race_settings import race_settings
import racr.settings.race_settings as rs
import racr.settings.lane_settings as ls
from .pit_settings import pit_settings
from .lane_settings import lane_settings
import json
import os

track_settings={
    'race': race_settings,
    'pit': pit_settings
}
track_settings.update(lane_settings)

def save_settings(name: str = "settings"):
    try:
        stored_settings = []
        for group in track_settings:
            settings = track_settings[group]
            for setting in settings:
                stored_settings.append({
                    'group': group,
                    'name': setting,
                    'value': settings[setting].value
                })
        with open(f'{name}.json', 'w') as outfile:
            json.dump(stored_settings, outfile, indent=2)
    except Exception as err:
        print(err)

async def load_settings(track_mgr: TrackManager, name: str = "settings"):
    rs.track = track_mgr
    ls.track = track_mgr
    try:
        with open(f'{name}.json') as jsonfile:
            stored_settings = json.load(jsonfile)
            for setting in stored_settings:
                try:
                    await track_settings[setting['group']][setting['name']].set_value(setting['value'])
                except Exception as err:
                    print(f'Error restoring setting {setting["name"]}: {err}')
    except Exception as err:
        print(err)

def list_settings() -> List[str]:
    settings = []
    for x in os.listdir():
        if x.endswith('json'):
            settings.append(x[0:-5])
    return settings