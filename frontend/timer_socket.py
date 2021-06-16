import socketio
import json

lanes=[]
connected=False

sio = socketio.Client()

def connectIfNeeded(ip):
    global connected
    if not connected:
        try:
            sio.connect(f'http://{ip}:80')
            connected=True
        except:
            connected=False

@sio.event
def connect():
    sio.emit('update')

@sio.event
def update(data):
    global lanes
    lanes=json.loads(data)
    lanes.sort(key=lambda l: l['pos'])
    print(lanes)

def get_lanes(ip='127.0.0.1'):
    connectIfNeeded(ip)
    sio.sleep(.001)
    return lanes

def disconnect():
    sio.disconnect()