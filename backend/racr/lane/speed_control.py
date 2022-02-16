from racr.flags import Flags

class SpeedControl():
    def __init__(self, io_manager, lane):
        self.io_manager = io_manager
        self.lane = lane
        self.slow = False
        self.stop = False
        self.out_of_gas = False
        self.max_speed = 100
        self.update_speed()

    def set_speed(self, slow, stop, oog):
        self.slow = slow
        self.stop = stop
        self.out_of_gas = oog
        self.update_speed()

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed
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
            throttle=min(throttle, 50)
            self.set_lane_speed(throttle)
        else:
            self.set_lane_speed(throttle)

        self.throttle=throttle
        return throttle

    def set_lane_speed(self,speed):
        self.io_manager.lane_controller.set_lane(self.lane,speed)

    def set_lane_oog(self):
        self.io_manager.lane_controller.set_oog(self.lane, 35, 77, 0)
