import socketio
import json

lanes=[]
connected=False

sio = socketio.Client()

def connectIfNeeded():
    global connected
    if not connected:
        try:
            #sio.connect('http://192.168.1.74:5000')
            sio.connect('http://127.0.0.1:5000')
            connected=True
        except:
            connected=False


@sio.event
def update(data):
    global lanes
    lanes=json.loads(data)
    lanes.sort(key=lambda l: l['pos'])
    print(lanes)

def get_lanes():
    connectIfNeeded()
    sio.sleep(.03)
    return lanes

def disconnect():
    sio.disconnect()