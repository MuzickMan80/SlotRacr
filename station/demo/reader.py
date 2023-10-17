import usb.core 
import usb.util 
import time 
import requests 
import json 
from pygame import mixer

mixer.init()
# import RPi.GPIO as GPIO 
 
USB_IF      = 0 # Interface 
USB_TIMEOUT = 5 # Timeout in MS 
USB_VENDOR  = 0xffff # Vendor-ID:  
USB_PRODUCT = 0x0035 # Product-ID 
 
# Find the HID device by vender/product ID
dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT) 

if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
#dev.set_configuration()

# Get and store the endpoint 
print(dev)
endpoint = dev[0][(0,0)][0] 
print(endpoint)
if dev.is_kernel_driver_active(USB_IF) is True: 
    print("Detaching kernel driver")
    dev.detach_kernel_driver(USB_IF) 

#dev.reset()

# Claim the device 
usb.util.claim_interface(dev, USB_IF) 

# Configure the Raspberry Pi GPIO
#GPIO.setmode(GPIO.BOARD) 
#GPIO.setup(11, GPIO.OUT) 
 
receivedNumber = 0 
while True: 
    control = None 
     
    try: 
        # Read a character from the device 
        control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT)
        
        #print(control)
        #print(control[0])
        #print(control[2])

        # Here you have to analyze what's coming in.
        # array('B', [0, 0, 40, 0, 0, 0, 0, 0])
        # In my case you had to check the first byte (command)
        if control[0] == 0 and not control[2] == 0 and not control[2] == 40:
            # Convert ascii to a number, there's probably better ways to do so.
            receivedDigit = control[2] - 29 
            #print(receivedDigit)

            if receivedDigit == 10: 
                receivedDigit = 0
                
            # Append the digit to the number
            receivedNumber = 10 * receivedNumber + receivedDigit 
            #print(receivedNumber)

        # Check if the received character is CRLF
        if (( control[0] == 0 )) and (( control[2] == 40 )) and (( not receivedNumber == 0 )): 
            # resp = requests.post("http://127.0.0.1/verify-access.php",data={'cardNumber':receivedNumber});
            # print "card: " + str(receivedNumber)             
            # ret_data = json.loads(resp.text) 
            # print ret_data["message"] 
            # print ret_data["can_enter"] 
            #if ret_data["can_enter"] == "1":
                # print "student: " + ret_data["student"]
                
                # Start the machine
                # GPIO.output(11, GPIO.HIGH) 
                # time.sleep(1) 
                # GPIO.output(11, GPIO.LOW) 
            # print 
            print(receivedNumber)
            if receivedNumber == 3317689:
                print('playing elliot')
                mixer.music.load('elliot.mp3')
                mixer.music.play()
            if receivedNumber == 3317753:
                print('playing dale')
                mixer.music.load('dale.mp3')
                mixer.music.play()
            if receivedNumber == 3264498:
                print('playing joe')
                mixer.music.load('joe.mp3')
                mixer.music.play()

            print('done')
            receivedNumber = 0 
    except KeyboardInterrupt: 
        #GPIO.cleanup() 
        pass
    except Exception as e:
        #print(e)
        pass 
     
    time.sleep(0.001) # Let CTRL+C actually exit 
