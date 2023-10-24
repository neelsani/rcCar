from udpHandler import udpServer

server = udpServer()

while True:
    print(server.recieve())