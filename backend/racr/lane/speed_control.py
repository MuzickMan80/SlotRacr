from racr.flags import Flags

class SpeedControl():
    def __init__(self, io_manager, lane):
        self.io_manager = io_manager
        self.lane = lane
        self.slow = False
        self.stop = False
        self.out_of_gas = False
        self.max_speed = 100
        self.warn_speed = 40
        self.speed = -2
        self.update_speed()

    def set_speed(self, slow, stop, oog):
        self.slow = slow
        self.stop = stop
        self.out_of_gas = oog
        self.oog_duty = 35
        self.oog_on_pwr = 77
        self.oog_off_pwr = 0
        self.update_speed()

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed
        self.update_speed()

    def set_warn_speed(self, warn_speed):
        self.warn_speed = warn_speed
        self.update_speed()

    def set_oog_duty(self, duty):
        self.oog_duty = duty
        self.update_speed()

    def set_oog_on(self, pwr):
        self.oog_on_pwr = pwr
        self.update_speed()

    def set_oog_off(self, pwr):
        self.oog_off_pwr = pwr
        self.update_speed()

    def update_speed(self):
        throttle = self.max_speed
        if self.stop:
            self.set_lane_speed(0)
            throttle = 0
        elif self.out_of_gas:
            throttle=min(throttle, 25)
            self.set_lane_oog()
        elif self.slow:
            throttle=min(throttle, self.max_speed * self.warn_speed / 100)
            self.set_lane_speed(throttle)
        else:
            self.set_lane_speed(throttle)

        self.throttle=throttle
        return throttle

    def set_lane_speed(self,speed):
        if self.speed != speed:
            self.speed = speed
            self.io_manager.lane_controller.set_lane(self.lane,speed)

    def set_lane_oog(self):
        if self.speed != -1:
            self.speed = -1
            self.io_manager.lane_controller.set_oog(self.lane, 35, 77, 0)
