from udpHandler import udpClient
import datetime
import threading
import time
server = udpClient(remote_ip="10.241.1.4",remote_port=7878,buffer_size=1028)
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
        

        server.send(str.encode("client----"+ str(datetime.datetime.now())))
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
    #print(server.packRecv)
    try:
        
        print(recvData[0])
    except KeyboardInterrupt:
        break

exitVal = True

time.sleep(2)
print(sd.is_alive())
print(rc.is_alive())

