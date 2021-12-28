
class RaceMode:
    Normal=1
    TimeTrials=2

class RaceType:
    def __init__(self,name,laps=None,mode:RaceMode=RaceMode.Normal):
        self.name = name
        self.laps = laps
        self.mode = mode

race_types = {
    RaceType("200 Lap Race", laps=200),
    RaceType("100 Lap Race", laps=100),
    RaceType("50 Lap Race", laps=50),
    RaceType("Time Trials", mode=RaceMode.TimeTrials)
}
