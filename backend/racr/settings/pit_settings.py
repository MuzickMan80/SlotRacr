
from racr.settings.setting import BoolSetting,IntSetting
import racr.settings.race_settings as race_settings

def set_require_crew_alert(require):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.require_crew_alert = require

require_crew_alert=BoolSetting("Require Crew Alert",True,"Require driver to press button on lap they wish to pit on",setter=set_require_crew_alert)

def set_laps_until_low(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.laps_until_low = laps

def set_max_laps_after_out(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.max_laps_after_out = laps

def set_mean_laps_after_out(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.mean_laps_after_out = laps

laps_until_low=IntSetting("Laps Until Out",45,min=0,max=1000,units="laps",
    description="Number of laps until out of gas",setter=set_laps_until_low)

max_laps_after_out=IntSetting("Max Laps After Out",7,min=0,max=100,units="laps",
    description="Number of laps until out of gas",setter=set_max_laps_after_out)

mean_laps_after_out=IntSetting("Mean Laps After Out",5,min=0,max=100,units="laps",
    description="Number of laps until out of gas",setter=set_mean_laps_after_out)

pit_settings={
    'require_crew_alert': require_crew_alert,
    'laps_until_low': laps_until_low,
    'max_laps_after_out': max_laps_after_out,
    'mean_laps_after_out': mean_laps_after_out
}
