import socket
from threading import Thread
from request import action_request
import json

host = "127.0.1.1"
port = 5000


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        Thread(target=self.connect_client).start()
        print(f"Сервер запущен! порт - {self.host}{self.port}")

    def send_message(self, client_socket, message):
        message = json.dumps(message)
        client_socket.send(message.encode())

    def get_message(self, client_socket):
        while True:
            request = client_socket.recv(2048)
            if request:
                data = json.loads(request)
                response, status = action_request(data)
                if status:
                    self.send_message(client_socket, response)

    def connect_client(self):
        while True:
            client_socket, addr = self.server.accept()
            print(f"клиент {addr} подключен!")
            if client_socket not in self.clients:
                self.clients.append(client_socket)
                Thread(target=self.get_message, name=addr[1], args=(client_socket,)).start()
                # client_socket.send("Вы успешно подключились!".encode())


Server(host=host, port=port)
