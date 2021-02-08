import socketio
import json

lanes=[]

sio = socketio.Client()
sio.connect('http://192.168.1.74:5000')

@sio.event
def update(data):
    global lanes
    lanes=json.loads(data)
    lanes.sort(key=lambda l: l['pos'])
    print(lanes)

def get_lanes():
    sio.sleep(.03)
    return lanes

def disconnect():
    sio.disconnect()