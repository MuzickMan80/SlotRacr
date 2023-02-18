
class LanePower:
    def __init__(self):
        self.powerPercent = 0
        self.onDutyPercent = 0
        self.offDutyPercent = 0
    def __eq__(self, other):
        return self.powerPercent == other.powerPercent and \
            self.onDutyPercent == other.onDutyPercent and \
            self.offDutyPercent == other.offDutyPercent

    def nudge_val(self, val, target):
        nudge_percent = 2
        if val < target:
            val = val + nudge_percent
            return val if val < target else target
        else:
            val = val - nudge_percent
            return val if val > target else target
    
    def nudge(self, target: 'LanePower'):
        self.powerPercent = self.nudge_val(self.powerPercent, target.powerPercent)
        self.onDutyPercent = self.nudge_val(self.onDutyPercent, target.onDutyPercent)
        self.offDutyPercent = self.nudge_val(self.offDutyPercent, target.offDutyPercent)
    