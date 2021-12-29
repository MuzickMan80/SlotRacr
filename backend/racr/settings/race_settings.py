
from racr.settings.setting import BoolSetting

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

race_settings=[
    enable_pitting
]
