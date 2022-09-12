
from racr.settings.setting import BoolSetting,IntSetting,FloatSetting
import racr.settings.race_settings as race_settings

def set_require_crew_alert(require):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.require_crew_alert = require

require_crew_alert=BoolSetting("Require Crew Alert",True,"Require driver to press button on lap they wish to pit on",setter=set_require_crew_alert)

def set_laps_until_low(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.laps_until_low = laps

laps_until_low=IntSetting("Laps Until Low",45,min=0,max=1000,units="laps",
    description="Number of laps until low on gas",setter=set_laps_until_low)

def set_max_laps_after_low(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.max_laps_after_low = laps

max_laps_after_low=IntSetting("Max Laps After Low",7,min=0,max=100,units="laps",
    description="Max number of laps until out of gas",setter=set_max_laps_after_low)

def set_mean_laps_after_low(laps):
    for lane in range(8):
        race_settings.track.lanes[lane].fuel.mean_laps_after_low = laps

mean_laps_after_low=IntSetting("Mean Laps After Low",5,min=0,max=100,units="laps",
    description="Mean number of laps until out of gas",setter=set_mean_laps_after_low)

def set_min_pit_time(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.min_pit_time = seconds

min_pit_time=FloatSetting("Minimum pit time",8,min=0,max=100,units="seconds",
    description="Minimum pit time",setter=set_min_pit_time)

def set_max_pit_time(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.max_pit_time = seconds

max_pit_time=FloatSetting("Maximum pit time",40,min=0,max=100,units="seconds",
    description="Maximum pit time",setter=set_max_pit_time)

def set_typical_pit_time(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.pit_time_mode = seconds

typical_pit_time=FloatSetting("Typical pit time",12,min=0,max=100,units="seconds",
    description="Typical pit time",setter=set_typical_pit_time)

def set_typical_pit_time_concentration(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.pit_time_concentration = seconds

typical_pit_time_concentration=FloatSetting("Typical pit time concentration",15,min=0,max=100,units="",
    description="Typical pit time concentration",setter=set_typical_pit_time_concentration)

def set_oof_pit_penalty(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.out_of_fuel_penalty = seconds

out_of_fuel_pit_penalty=FloatSetting("Out of fuel pit penalty",10,min=0,max=100,units="",
    description="Out of fuel pit penalty" ,setter=set_oof_pit_penalty)

def set_accident_pit_penalty(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.accident_penalty = seconds

out_of_fuel_pit_penalty=FloatSetting("Accident pit penalty",30,min=0,max=100,units="",
    description="Accident pit penalty" ,setter=set_accident_pit_penalty)

def set_max_crew_alert_time(seconds):
    for lane in range(8):
        race_settings.track.lanes[lane].pit.max_crew_alert_time = seconds

max_crew_alert_time=FloatSetting("Max crew alert time",2,min=0,max=10,units="seconds",
    description="Max crew alert time",setter=set_max_crew_alert_time)

pit_settings={
    'require_crew_alert': require_crew_alert,
    'max_crew_alert_time': max_crew_alert_time,
    'laps_until_low': laps_until_low,
    'max_laps_after_low': max_laps_after_low,
    'mean_laps_after_low': mean_laps_after_low,
    'min_pit_time': min_pit_time,
    'max_pit_time': max_pit_time,
    'typical_pit_time': typical_pit_time,
    'typical_pit_time_concentration': typical_pit_time_concentration
}
