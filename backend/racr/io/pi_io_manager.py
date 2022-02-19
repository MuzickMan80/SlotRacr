from .io_manager import IoManager
import pigpio

reset_pin = 4
lane_pins = [17,27,22,5,6,13,19,26]
pit_pins = [-1,-1,-1,-1,-1,-1,-1,-1]

class PiIoManager(IoManager):
    def __init__(self, async_loop, ip=None):
        super().__init__(async_loop)

        if ip:
            self.pi = pigpio.pi(ip)
        else:
            self.pi = pigpio.pi()

        if not self.pi.connected:
            print('Failed to connect to pigpio server')
            exit()

        print('gpio connection succeeded')

    def current_ticks(self):
        return self.pi.get_current_tick()

    def get_lane_pin(self, lane) -> int:
        return lane_pins[lane]

    def get_reset_pin(self) -> int:
        return reset_pin

    def get_pit_pin(self, lane) -> int:
        return pit_pins[lane]

    def tick_diff_micros(self, start, end):
        return pigpio.tickDiff(start, end)

    def monitor_pin(self, pin, cb, rising=True, falling=False, pullUp=False, pullDown=False, filterUs=0):
        self._register_callback(pin, cb)

        self.pi.set_mode(pin, pigpio.INPUT)
        if pullUp:
            self.pi.set_pull_up_down(pin, pigpio.PUD_UP)
        elif pullDown:
            self.pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        else:
            self.pi.set_pull_up_down(pin, pigpio.PUD_OFF)

        if filterUs > 0:
            self.pi.set_glitch_filter(pin, filterUs)

        if rising and falling:
            self.pi.callback(pin, 2, self._io_update)
        elif rising:
            self.pi.callback(pin, 1, self._io_update)
        elif falling:
            self.pi.callback(pin, 0, self._io_update)
