from racr.io.led_controller import LedController
from racr.flags import Flags

class LightMap():
    green = 0
    yellow = 1
    red = 2

class TrackLights:
    def __init__(self, controller: LedController, track):
        self.controller = controller
        self.track = track
        self.track.add_observer(self.update)
        self.flag = None

    def update(self):
        if self.track.flag == self.flag:
            return
        self.flag = self.track.flag
        if self.flag == Flags.green or self.flag == Flags.white:
            self.controller.set_light(LightMap.green, True)
            self.controller.set_light(LightMap.yellow, False)
            self.controller.set_light(LightMap.red, False)
        elif self.flag == Flags.yellow or self.flag == Flags.checkered:
            self.controller.set_light(LightMap.green, False)
            self.controller.set_light(LightMap.yellow, True)
            self.controller.set_light(LightMap.red, False)
        elif self.flag == Flags.red:
            self.controller.set_light(LightMap.green, False)
            self.controller.set_light(LightMap.yellow, False)
            self.controller.set_light(LightMap.red, True)
        elif self.flag == Flags.checkered:
            self.controller.set_light(LightMap.green, False)
            self.controller.set_light(LightMap.yellow, True)
            self.controller.set_light(LightMap.red, False)
