import socket


class Socketserver:
    def __init__(self, address, port):
        self.port = port
        self.address = address

    def runserver(self, q):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.address, self.port))
        s.listen(q)
    
        while True:
            clientSocket, address = s.accept()
            print(f"Connection from {address} has been established!")
            clientsocket.send(bytes("Welcome to the server!", 'utf-8'))
            clientsocket.close()
