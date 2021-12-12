from io_manager import IoManager
import pigpio

class PiIoManager(IoManager):
    def __init__(self, async_loop):
        super().__init__(async_loop)
        self.pi = pigpio.pi()

        if not self.pi.connected:
            print('Failed to connect to pigpio server')
            exit()

        print('gpio connection succeeded')

    def tick_diff(self, start, end):
        return pigpio.tickDiff(start, end)

    def monitor_pin(self, pin, cb, rising=True, falling=False, pullUp=False, pullDown=False):
        self._register_callback(pin, cb)

        self.pi.set_mode(pin, pigpio.INPUT)
        if pullUp:
            self.pi.set_pull_up_down(pin, pigpio.PUD_UP)
        elif pullDown:
            self.pi.set_pull_up_down(pin, pigpio.PUD_DOWN)
        else:
            self.pi.set_pull_up_down(pin, pigpio.PUD_OFF)
            
        print(pin, self.pi.read(pin))

        if rising and falling:
            self.pi.callback(pin, 2, self._io_update)
        elif rising:
            self.pi.callback(pin, 1, self._io_update)
        elif falling:
            self.pi.callback(pin, 0, self._io_update)
