class LaneStateReporter:
    def __init__(self, lane, timer, pit, fuel):
        self.lane = lane
        self.timer = timer
        self.pit = pit
        self.fuel = fuel

    def report_state(self):
        lane = self.lane
        timer = self.timer
        return {
            'lane': lane.lane+1,
            'best': self.time_string(timer.best),
            'last': self.time_string(timer.last),
            'laps': timer.laps,
            'pos': timer.pos,
            'started': timer.started,
            'name': lane.name,
            'color': lane.color,
            'state': self.get_indicator(),
            'pitinfo': self.get_pit_info(),
            'pittime': self.pit.pit_time,
            'accident': self.pit.accident
            }

    def time_string(self, time):
        s = 0
        if time:
            s = time / 1000000
            return round(s,3)
        else:
            return None

    def get_indicator(self) -> str:
        if self.pit.in_pits:
            return f'{self.pit.pit_progress:.1f}'
        if self.pit.pitting:
            return "slo"
        if self.pit.pit_this_lap:
            return "pit"
        if self.fuel.out_of_fuel:
            return "out"
        if self.fuel.low_fuel:
            return "lgas"
        if self.pit.accident:
            return "acdt"
        if self.pit.penalty:
            return "plty"
        return "go"

    def get_pit_info(self) -> str:
        if self.pit.in_pits:
            return self.pit.pit_info
        else:
            return ""