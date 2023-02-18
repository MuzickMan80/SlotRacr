from racr.flags import Flags
import logging

logger = logging.getLogger(__name__)

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
        self.oog_duty = 35
        self.oog_on_pwr = 100
        self.oog_off_pwr = 0
        self.damage = 0
        self.damage_penalties = [50, 15, 8]
        self.update_speed()

    def set_speed(self, slow, stop, oog, damage):
        self.slow = slow
        self.stop = stop
        self.out_of_gas = oog
        self.damage = damage
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

    def calculate_damage_penalty(self):
        num_penalties = len(self.damage_penalties)
        penalty = 0
        damage_counter = 0
        while damage_counter < self.damage:
            if damage_counter < num_penalties:
                penalty = penalty + self.damage_penalties[damage_counter]
            else:
                penalty = penalty + self.damage_penalties[-1]
            damage_counter = damage_counter + 1
        return penalty * .01 * self.max_speed

    def update_speed(self):
        throttle = self.max_speed - self.calculate_damage_penalty()
        if self.stop:
            self.set_lane_speed(0,immediate=True)
            throttle = 0
        elif self.out_of_gas:
            throttle=min(throttle, 25)
            self.set_lane_oog()
        elif self.slow:
            throttle=min(throttle, self.warn_speed)
            self.set_lane_speed(throttle)
        else:
            self.set_lane_speed(throttle)

        self.throttle=throttle
        return throttle

    def set_lane_speed(self,speed,immediate:bool=False):
        if self.speed != speed:
            logger.debug('set_lane_speed %d', speed)
            self.speed = speed
            self.io_manager.lane_controller.set_oog(self.lane, self.oog_duty, speed, speed, immediate)

    def set_lane_oog(self):
        if self.speed != -1:
            logger.debug('set_lane_oog')
            self.speed = -1
            self.io_manager.lane_controller.set_oog(self.lane, self.oog_duty, self.oog_on_pwr, self.oog_off_pwr)
