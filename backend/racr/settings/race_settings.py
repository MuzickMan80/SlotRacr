
from racr.settings.setting import StringSetting
from racr.settings.setting import BoolSetting

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

class LaneNameSetting(StringSetting):
    def __init__(self, lane):
        super().__init__(f"Lane {lane} Name")

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

race_settings={
    'enable_pitting': enable_pitting
}

lane_name=[]

def set_lane_name(i, name):
    
for i in range(8):
    setter=lambda val,track: (track.lanes[i].name := val)
    lane_name.append(LaneNameSetting(i+1,setter))
    race_settings[f'lane{i+1}_name'] = lane_name[i] 
