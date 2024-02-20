import evdev
from evdev import ecodes, categorize

class CardReader():
    def __init__(self):
        self.device = self._find_event_device()
        self.buffer = 0


    def read(self) -> int:
        if self.device == None:
            self.device = self._find_event_device()

        while self.device:
            try:
                event = self.device.read_one()
                if event:
                    if event.type == ecodes.EV_KEY and event.value == 1:
                        if event.code == ecodes.KEY_ENTER:
                            ret = int(self.buffer)
                            self.buffer = 0
                            return ret
                        elif event.code >= ecodes.KEY_1 and event.code <= ecodes.KEY_0:
                            num = event.code - ecodes.KEY_1 + 1
                            if num == 10:
                                num = 0
                            self.buffer = self.buffer * 10 + num
                else:
                    break
            except Exception as e:
                print(f"Error reading from {self.device}: {e}")
                self.device = None

        return None


    def _find_event_device(self):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if str(device.name).find("Sycreader") != -1:
                print(device)
                device.grab()
                return device