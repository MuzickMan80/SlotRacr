
from racr.settings.setting import StringSetting
from racr.settings.setting import BoolSetting, IntSetting, FloatSetting
from racr.track_manager import TrackManager
from asyncio import run

track: TrackManager

class LaneNameSetting(StringSetting):
    def __init__(self, lane, setter):
        super().__init__(f"Lane {lane} Name",setter=setter)

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

num_laps=IntSetting("Number Of Laps", 100, 1, 1000, "Laps", "Number of laps in the race",
    setter=lambda x: setattr(track, "num_laps", x))

enable_simulator=BoolSetting("Enable simulator", False, "Enables an event simulator for testing",
    setter=lambda x: track.enable_activity_simulator(x,1))

minimum_lap_time=FloatSetting("Minimum lap time", 4, 0.5, 10, "Seconds", "Minimum lap time",
    setter=lambda x: map(lambda lane: setattr(lane, "minimum_lap_time", x), track.lanes))

race_settings={
    'enable_pitting': enable_pitting,
    'number_of_laps': num_laps,
    'enable_simulator': enable_simulator,
    'minimum_lap_time': minimum_lap_time
}

def get_lane_name_setter(i):
    async def lane_name_setter(name):
        track.lanes[i].name = name
        await track.notify_observer_async()
    return lane_name_setter

def set_lane_speed(i, speed):
    track.lanes[i].speed.set_max_speed(speed)

for i in range(8):
    race_settings[f'lane{i+1}_name'] = LaneNameSetting(i+1,setter=get_lane_name_setter(i))
    race_settings[f'lane{i+1}_maxspeed'] = IntSetting(f'Lane {i+1} speed', 100, 1, 100, "Percent", 
        setter=lambda s,i=i: set_lane_speed(i,s))
