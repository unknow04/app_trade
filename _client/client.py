import socket
import time
from threading import Thread


class SocketClient:
    address = socket.gethostbyname(socket.gethostname())
    print(address)  # as both code is running on same pc
    port = 5000

    def __init__(self, ip=address, port=port):
        self.ip = ip
        self.port = port
        self.client = None

    def connect_server(self, ip, port):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, port))
            return {"message": 200}, self.client
        except:
            return {"message": 400}, None

    def get_response(self):
        data = self.client.recv(2048).decode()
        return data

    def message(self, message):
        data = message.encode()
        self.client.send(data)
        if message == b"exit":
            self.client.close()
