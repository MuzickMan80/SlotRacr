import serial
import asyncio
from .button import Button

lane_mappings = [
    (1,0),
    (1,1),
    (1,2),
    (1,3),
    (0,0),
    (0,1),
    (0,2),
    (0,3)
]

class LaneController:
    def __init__(self):
        self.ports = []
        try:
            self.ports.append(serial.Serial('/dev/ttyACM0', 500000))
            print("Opened serial port to lane controller 1")
            self.ports.append(serial.Serial('/dev/ttyACM1', 500000))
            print("Opened serial port to lane controller 2")
            self.tasks = []
            self.start_polling()
            self.button_handlers = []
            self.last_state = []
            for i in range(8):
                self.button_handlers.append(None)
                self.last_state.append(False)
            print(self.button_handlers)
            
            for i in range(8):
                try:
                    self.set_light(i,1)
                except:
                    pass
                try:
                    self.set_light(i,0)
                except:
                    pass

        except Exception as ex:
            print(f"Failed to open serial port: {ex}")

    def start_polling(self):
        loop = asyncio.get_event_loop()
        if self.ports[0]:
            self.tasks.append(loop.create_task(self.poll_loop()))
        if self.ports[1]:
            self.tasks.append(loop.create_task(self.poll_loop()))

    def get_lane(self,port,pin):
        for lane in range(8):
            lane_map = lane_mappings[lane]
            if lane_map[0] == port and lane_map[1] == pin:
                return lane
        return -1

    async def poll_loop(self):
        while True:
            for port in range(2):
                try:
                    response = self.send_command(port,'r')
                    button=0
                    for char in response:
                        if button >= 8:
                            break
                        button_state = char == '1'
                        lane = self.get_lane(port, button) 
                        if lane != -1:
                            if button_state != self.last_state[lane]:
                                self.last_state[lane] = button_state
                                handler = self.button_handlers[lane]
                                if handler:
                                    await handler(button_state)
                        button = button + 1
                except Exception as err:
                    print(f'Error occurred reading buttons from {port}: {err}')

            await asyncio.sleep(.01)

    def send_command(self, port, command):
        response = None
        self.ports[port].writelines([command.encode(), b'\r'])
        print(f'command: "{command}"')
        while True:
            line = self.ports[port].readline().decode()
            print(f'response: "{line}"')
            if line == "ok\r\n":
                break
            elif line == "err\r\n":
                raise Exception("Error sending command")
            elif line == "\r\n":
                break
            else:
                response = line
        return response

    def monitor_button(self, button, handler):
        self.button_handlers[button] = handler

    def set_frequency(self, freq=100):
        self.send_command(0,f'f{freq}')
        self.send_command(1,f'f{freq}')

    def set_oog_freq(self, freq=6):
        period=round(1000/freq)
        self.send_command(0,f's{period}')
        self.send_command(1,f's{period}')

    def set_lane(self, lane, percent=0):
        self.set_oog(lane, percent, 100, 0)

    def set_oog(self, lane, percent, onPercent, offPercent):
        lane_map = lane_mappings[lane]
        on_time = 65535*(percent/100)
        on_pwr = 65535*(onPercent/100)
        off_pwr = 65535*(offPercent/100)
        self.send_command(lane_map[0],f'g{lane_map[1]},{on_time},{on_pwr},{off_pwr}')        

    def set_light(self, light, on):
        lane_map = lane_mappings[light]
        on_val = 0
        if on:
            on_val = 1
        self.send_command(lane_map[0],f'w{lane_map[1]},{on_val}')
