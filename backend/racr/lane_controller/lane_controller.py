import serial
import asyncio
from .button import Button

lane_mappings = [
    (1,0),
    (1,1),
    (1,6),
    (1,3),
    (0,0),
    (0,1),
    (0,4),
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

            await asyncio.sleep(.01)

    def send_command(self, port, command):
        response = None
        self.ports[port].writelines([command.encode(), b'\r'])
        #print(f'command: "{command}"')
        while True:
            line = self.ports[port].readline().decode()
            #print(f'response: "{line}"')
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

    def set_lane(self, lane, percent=0, freq=100):
        lane_map = lane_mappings[lane]
        on_time = 65535*(percent/100)
        self.send_command(lane_map[0],f'o{lane_map[1]},{on_time}')
        if percent != 0 and percent != 100:
            self.send_command(lane_map[0],f'f{lane_map[1]},{freq}')

    def set_light(self, light, on):
        lane_map = lane_mappings[light]
        on_val = 0
        if on:
            on_val = 1
        self.send_command(lane_map[0],f'w{lane_map[1]},{on_val}')