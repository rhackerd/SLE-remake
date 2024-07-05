import socket
from mains.engine.constants import LOAD

player_name = "rhacker_8853"

class Client:
    def __init__(self, host, port, chat):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        self.chat = chat
        self.onStart()

    def step(self):
        # Placeholder for future PING request or other operations
        pass

    def onStart(self):
        self.socket.send(LOAD.to_bytes(4, byteorder='big'))
        self.socket.send(player_name.encode())
        response = self.socket.recv(1024).decode()
        self.chat.print_message(response)
        self.close_connection()

    def close_connection(self):
        self.socket.close()
        print("Disconnected from server")

if __name__ == "__main__":
    # Mock chat object for testing
    class Chat:
        def print_message(self, message):
            print(f"Server: {message}")

    client = Client("127.0.0.1", 12345, Chat())  # Adjust IP and Port if necessary
    client.step()
    client.close_connection()
