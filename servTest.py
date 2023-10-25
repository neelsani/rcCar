from udpHandler import udpServer
import datetime
import threading
import time
server = udpServer(listen_ip="10.241.1.4", listen_port=7878, buffer_size=1024)
exitVal = False
recvData = [None,(None,None)]
#remote = ("10.241.1.3",7878)
def serRecv():
    global server, recvData, evitVal
    while True:

        recvData = server.recieve()
        if exitVal:
            break
    return
def serSend():
    global server, exitVal

    while True:
        if server.packRecv:

            server.send(str.encode("server----"+ str(datetime.datetime.now())))
        if exitVal:
            break
    return
sd = threading.Thread(target=serSend, args=())
rc = threading.Thread(target=serRecv, args=())

sd.daemon = True
rc.daemon = True

sd.start()
rc.start()


while True:
    print(server.packRecv)
    try:
        continue
        #print(recvData[1][1])
    except KeyboardInterrupt:
        break

exitVal = True

time.sleep(2)
print(sd.is_alive())
print(rc.is_alive())

