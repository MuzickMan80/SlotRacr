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

def get_lane_color_setter(i):
    async def lane_color_setter(color):
        track.lanes[i].color = color
        await track.notify_observer_async()
    return lane_color_setter

def set_lane_speed(i, speed):
    track.lanes[i].speed.set_max_speed(speed)
    track.lanes[i].speed.set_oog_on(speed)

def set_lane_slow_speed(i, speed):
    track.lanes[i].speed.set_warn_speed(speed)

def set_lane_oof_duty(i, duty):
    track.lanes[i].speed.set_oog_duty(duty)

def set_lane_oof_off(i, speed):
    track.lanes[i].speed.set_oog_off(speed)

lane_settings = {}

for i in range(8):
    lane_settings[f'lane_{i+1}'] = {
        'name': LaneNameSetting(i+1,setter=get_lane_name_setter(i)),
        'color': StringSetting(f'Lane {i+1} Color', "green", setter=get_lane_color_setter(i)),
        'maxspeed': IntSetting(f'Lane {i+1} Speed', 100, 1, 100, "Percent", 
            setter=lambda s,i=i: set_lane_speed(i,s)),
        'slowspeed': IntSetting(f'Lane {i+1} Slow Speed', 40, 1, 100, "Percent", 
            setter=lambda s,i=i: set_lane_slow_speed(i,s)),
        'oof_duty': IntSetting(f'Lane {i+1} Out Of Gas Duty Cycle', 40, 1, 100, "Percent", 
            setter=lambda s,i=i: set_lane_oof_duty(i,s)),
        'oof_off': IntSetting(f'Lane {i+1} Out Of Gas Off Power', 20, 1, 100, "Percent", 
            setter=lambda s,i=i: set_lane_oof_off(i,s))
    }
