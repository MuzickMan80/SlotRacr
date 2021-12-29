
from racr.settings.setting import BoolSetting

require_crew_alert=BoolSetting("Require Crew Alert",True,"Require driver to press button on lap they wish to pit on")

pit_settings={
    'require_crew_alert': require_crew_alert
}
