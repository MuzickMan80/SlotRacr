
from racr.settings.setting import BoolSetting,IntSetting
import racr.settings.race_settings as race_settings

def set_require_crew_alert(require):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.require_crew_alert = require

require_crew_alert=BoolSetting("Require Crew Alert",True,"Require driver to press button on lap they wish to pit on",setter=set_require_crew_alert)

def set_laps_until_out(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.laps_until_out = laps

laps_until_out=IntSetting("Laps Until Out",45,min=0,max=1000,units="laps",
    description="Number of laps until out of gas",setter=set_laps_until_out)

pit_settings={
    'require_crew_alert': require_crew_alert,
    'laps_until_out': laps_until_out
}
