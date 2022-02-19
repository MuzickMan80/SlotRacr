# Contains per-lane settings
from racr.track_manager import TrackManager
from racr.settings.setting import StringSetting, IntSetting

track: TrackManager

class LaneNameSetting(StringSetting):
    def __init__(self, lane, setter):
        super().__init__(f"Lane {lane} Name",setter=setter)

def get_lane_name_setter(i):
    async def lane_name_setter(name):
        track.lanes[i].name = name
        await track.notify_observer_async()
    return lane_name_setter

def set_lane_speed(i, speed):
    track.lanes[i].speed.set_max_speed(speed)

lane_settings = {}

for i in range(8):
    lane_settings[f'lane_{i+1}'] = {
        'name': LaneNameSetting(i+1,setter=get_lane_name_setter(i)),
        'maxspeed': IntSetting(f'Lane {i+1} speed', 100, 1, 100, "Percent", 
            setter=lambda s,i=i: set_lane_speed(i,s))
    }
