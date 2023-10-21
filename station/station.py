import socket
import time
import usb.core
import usb.util
import requests
from pygame import mixer

backend_addr = None

class RaceStation:
    def __init__(self):
        self.read_lane()
        self.setup_udp()
        self.setup_reader()
        self.setup_sound()
        self.running = True

    def read_lane(self):
        with open('trackid', 'r') as f:
            self.lane = int(f.readline().strip())
            print(f'Lane {self.lane}')

    def run(self):
        print("Starting")
        while self.running:
            self.process_udp()
            self.process_reader()
            time.sleep(.001)

    def setup_udp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.1)
        self.sock.bind(("0.0.0.0", 5005))
        self.backend_addr = None
    
    def process_udp(self):
        try:
            data, addr = self.sock.recvfrom(5000)
            print("received message: %s" % str(data, encoding='utf-8'))
            print("msglen %d" % len(data))
        
            if self.backend_addr == None:
                self.backend_addr = addr
        except KeyboardInterrupt:
            print("Bye")
            self.running = False
        except:
            pass

    def setup_reader(self):
        USB_IF      = 0 # Interface 
        USB_VENDOR  = 0xffff # Vendor-ID:  
        USB_PRODUCT = 0x0035 # Product-ID 
 
        # Find the HID device by vender/product ID
        dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT) 

        if dev is None:
            raise ValueError('Device not found')

        if dev.is_kernel_driver_active(USB_IF) is True: 
            print("Detaching kernel driver")
            dev.detach_kernel_driver(USB_IF) 

        usb.util.claim_interface(dev, USB_IF)
        self.reader = dev
        self.received_number = 0

    def process_reader(self):
        while self.running:
            try:
                USB_TIMEOUT = 5 #milliseconds
                endpoint = self.reader[0][(0,0)][0]
                control = self.reader.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
                # Here you have to analyze what's coming in.
                # array('B', [0, 0, 40, 0, 0, 0, 0, 0])
                # In my case you had to check the first byte (command)
                if control[0] == 0 and not control[2] == 0 and not control[2] == 40:
                    # Convert ascii to a number, there's probably better ways to do so.
                    receivedDigit = control[2] - 29 

                    if receivedDigit == 10: 
                        receivedDigit = 0
                
                    # Append the digit to the number
                    self.received_number = 10 * self.received_number + receivedDigit 

                if (( control[0] == 0 )) and (( control[2] == 40 )) and (( not self.received_number == 0 )):
                    print(self.received_number)
                    self.process_badge(self.received_number)
                    self.received_number = 0

            except KeyboardInterrupt:
                print("Bye")
                self.running = False
            except usb.core.USBTimeoutError:
                break
            except Exception as ex:
                print(str(type(ex)) + str(ex))
                break

    def process_badge(self, badge):
        if self.backend_addr:
            addr,port = self.backend_addr
            lane = self.lane-1
            url = f'http://{addr}/registration/lane/{lane}/badge_id'
            print(f'Register {badge} at {self.backend_addr}')
            r = requests.put(url, data=str(badge))
            print(r)
            print(r.content)
            self.play_welcome_sound()

    def setup_sound(self):
        mixer.init()

        if self.lane == 8:
            mixer.music.load('race.wav')
            mixer.music.set_volume(0.2)
            mixer.music.play(loops=-1)
        if self.lane == 4:
            mixer.music.load('race.wav')
            mixer.music.set_volume(0.2)
            mixer.music.play(loops=-1)

    def play_welcome_sound(self):
        mixer.find_channel(force=True).play(mixer.Sound('media/04 - sound0.mp3'))

station = RaceStation()
station.run()

