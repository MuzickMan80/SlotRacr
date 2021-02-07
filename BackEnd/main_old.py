import pigpio
import time
import falcon
import json

pi = pigpio.pi('169.254.154.109')
if not pi.connected:
    print('Failed to connect to pigpio server')
    exit()

print('gpio connection succeeded')
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(4, pigpio.INPUT)

i=pi.read(4)
print(f'in={i}')
def cbf(event, level, tick):
    print(event, level, tick)

pi.callback(4, 1, cbf)
pi.hardware_PWM(18, 38000, 300000)
#pi.write(18, 1)
time.sleep(0.1)
i=pi.read(4)
print(f'in={i}')
time.sleep(5)
#pi.write(18, 0)
pi.hardware_PWM(18, 38000, 0000)

time.sleep(1)
i=pi.read(4)
print(f'in={i}')