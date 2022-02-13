from racr.track_manager import TrackManager
from .race_settings import race_settings
import racr.settings.race_settings as rs
from .pit_settings import pit_settings
import json

track_settings={
    'race': race_settings,
    'pit': pit_settings
}

def save_settings():
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
        with open('settings.json', 'w') as outfile:
            json.dump(stored_settings, outfile, indent=2)
    except Exception as err:
        print(err)

def load_settings(track_mgr: TrackManager):
    rs.track = track_mgr
    try:
        with open('settings.json') as jsonfile:
            stored_settings = json.load(jsonfile)
            for setting in stored_settings:
                try:
                    track_settings[setting['group']][setting['name']].value = setting['value']
                except Exception as err:
                    print(f'Error restoring setting {setting["name"]}: {err}')
    except Exception as err:
        print(err)