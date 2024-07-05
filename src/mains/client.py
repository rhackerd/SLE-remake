import socket
from classes.constants import PING, LOAD


player_name = "rhacker_8853"


class Client:
    def __init__(self, host, port, config):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_ping(self):
        self.socket.send(PING.to_bytes(4, byteorder='big'))  # Send 4 bytes (int)

    def join(self):
        self.socket.send(LOAD.to_bytes(4, byteorder='big'))
        self.socket.send(player_name.encode())

    def revc_raw_data(self):
        return self.socket.recv(1024)

    def ping_server(self):
        self.connect()
        self.send_ping()


    def close(self):
        self.socket.close()

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.send_ping()
    client.close()