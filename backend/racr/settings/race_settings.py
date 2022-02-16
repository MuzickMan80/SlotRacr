
from racr.settings.setting import StringSetting
from racr.settings.setting import BoolSetting, IntSetting
from racr.track_manager import TrackManager

track: TrackManager

class LaneNameSetting(StringSetting):
    def __init__(self, lane, setter):
        super().__init__(f"Lane {lane} Name",setter=setter)

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

num_laps=IntSetting("Number Of Laps", 100, 1, 1000, "Laps", "Number of laps in the race",
    setter=lambda x: setattr(track, "num_laps", x))

enable_simulator=BoolSetting("Enable simulator", False, "Enables an event simulator for testing",
    setter=lambda x: track.enable_activity_simulator(x,1))

race_settings={
    'enable_pitting': enable_pitting,
    'number_of_laps': num_laps,
    'enable_simulator': enable_simulator
}

def set_lane_name(i, name):
    track.lanes[i].name = name

def set_lane_speed(i, speed):
    track.lanes[i].pit.speed.set_max_speed(speed)

for i in range(8):
    race_settings[f'lane{i+1}_name'] = LaneNameSetting(i+1,setter=lambda n,i=i: set_lane_name(i,n))
    race_settings[f'lane{i+1}_maxspeed'] = IntSetting(f'Lane {i+1} speed', 100, 1, 100, "Percent", 
        setter=lambda s,i=i: set_lane_speed(i,s))
