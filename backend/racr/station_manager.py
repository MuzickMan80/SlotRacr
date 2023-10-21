import socket

STATION_MGR_ADDRESS = "192.168.2.2"
STATION_BROADCAST_ADDRESS = "192.168.2.255"
STATION_MGR_PORT = 5005

class StationManager:
    def __init__(self):
        self.broadcast_socket: socket.socket = None
        self.broadcast_addr = None
        self.bind()

    def update(self, payload: str):
        try:
            if self.broadcast_socket:
                self.broadcast_socket.sendto(payload, self.broadcast_addr)
        except Exception as ex:
            print("Failed to send station update: " + str(ex))

    def bind(self):
        try:
            self.broadcast_socket = socket.socket(  socket.AF_INET, # Internet
                                                    socket.SOCK_DGRAM) # UDP
            self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.broadcast_socket.bind((STATION_MGR_ADDRESS, STATION_MGR_PORT))
            self.broadcast_addr = (STATION_BROADCAST_ADDRESS, STATION_MGR_PORT)
        except Exception as ex:
            print("Failed to bind station broacast port: " + str(ex))
