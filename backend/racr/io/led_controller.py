import serial

class LedController: # pragma: no cover
    def __init__(self):
        self.port = None
        try:
            self.port = serial.Serial('/dev/ttyACM1', 500000, timeout=0.1)
            print("Opened serial port to led controller")
            
            for i in range(3):
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

    def set_light(self, light, on):
        on_val = 1 if on else 0
        self.send_command(f'w{light},{on_val}')
        
    def send_command(self, command):
        if not self.port:
            return

        response = None
        serport = self.port
        serport.reset_input_buffer()
        serport.writelines([command.encode(), b'\r'])
        # print(f'command: "{command}"')
        while True:
            line = serport.readline().decode()
            # print(f'response: "{line}"')
            if line == "ok\r\n":
                break
            elif line == "err\r\n":
                raise Exception("Error sending command")
            elif line == "\r\n":
                break
            else:
                response = line
        return response