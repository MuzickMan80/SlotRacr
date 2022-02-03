
from racr.settings.setting import StringSetting
from racr.settings.setting import BoolSetting
from racr.track_manager import TrackManager

track: TrackManager

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

class LaneNameSetting(StringSetting):
    def __init__(self, lane, setter):
        super().__init__(f"Lane {lane} Name",setter=setter)

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

race_settings={
    'enable_pitting': enable_pitting
}

lane_name=[]

def set_lane_name(i, name):
    track.lanes[i].name = name

for i in range(8):
    lane_name.append(LaneNameSetting(i+1,set_lane_name))
    race_settings[f'lane{i+1}_name'] = lane_name[i] 
