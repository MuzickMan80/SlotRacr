import serial
import asyncio
from .button import Button

class LaneController:
    def __init__(self):
        self.port = None
        try:
            self.port = serial.Serial('/dev/ttyACM0', 500000)
            self.start_polling()
            self.task = None
            self.button_handlers = []
            self.last_state = []
            for i in range(8):
                self.button_handlers.append(None)
                self.last_state.append(False)
        except Exception as ex:
            print(f"Failed to open serial port: {ex}")

    def start_polling(self):
        if self.port:
            loop = asyncio.get_event_loop()
            self.task = loop.create_task(self.poll_loop())
            
    async def poll_loop(self):
        while True:
            response = self.send_command('r')
            button=0
            for char in response:
                if button >= 8:
                    break
                button_state = char == '1'
                if button_state != self.last_state[button]:
                    self.last_state[button] = button_state
                    handler = self.button_handlers[button]
                    if handler:
                        await handler(button_state)

            await asyncio.sleep(.01)

    def send_command(self, command):
        response = None
        self.port.writelines([command.encode(), b'\n'])
        print(command)
        while True:
            line = self.port.readline().decode()
            print(line)
            if line == "ok\r\n":
                break
            elif line == "err\r\n":
                raise Exception("Error sending command")
            else:
                response = line
        return response

    def monitor_button(self, button, handler):
        self.button_handlers[button] = handler

    def set_lane(self, lane, percent=0, freq=100):
        on_time = 65535*(percent/100)
        self.send_command(f'o{lane},{on_time}')
        if percent != 0 and percent != 100:
            self.send_command(f'f{lane},{freq}')

    def set_light(self, light, on):
        on_val = 0
        if on:
            on_val = 1
        self.send_command(f'w{light},{on_val}')