from udpHandler import udpServer
import datetime
import threading
server = udpServer(listen_ip="10.241.1.4", listen_port=7878, buffer_size=1024)

recvData = None
remote = ("10.241.1.3",7878)
def serRecv():
    global server, recvData
    while True:

        recvData = server.recieve()
def serSend():
    global server, remote

    while True:
        server.send(str.encode("server----"+ str(datetime.datetime.now())), remote)

sd = threading.Thread(target=serSend, args=())
rc = threading.Thread(target==serRecv, args=())

sd.daemon = True
rc.daemon = True

sd.start()
rc.start()


while True:

    
    print(recvData[0])