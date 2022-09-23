from racr.settings.setting import BoolSetting, IntSetting, FloatSetting
from racr.track_manager import TrackManager

track: TrackManager

enable_pitting=BoolSetting("Enable Pitting",True,"Require drivers to perform Pit Stops during the race")

num_laps=IntSetting("Number Of Laps", 100, 1, 1000, "Laps", "Number of laps in the race",
    setter=lambda x: setattr(track, "num_laps", x))

async def set_enable_simulator(enable):
    await track.enable_activity_simulator(enable, 1)

enable_simulator=BoolSetting("Enable simulator", False, "Enables an event simulator for testing",
    setter=set_enable_simulator)

minimum_lap_time=FloatSetting("Minimum lap time", 4, 0.5, 10, "Seconds", "Minimum lap time",
    setter=lambda x: map(lambda lane: setattr(lane.timer, "minimum_lap_time", x), track.lanes))

race_settings={
    'enable_pitting': enable_pitting,
    'number_of_laps': num_laps,
    'enable_simulator': enable_simulator,
    'minimum_lap_time': minimum_lap_time
}
