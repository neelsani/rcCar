from udpHandler import udpServer
import threading
from mDev import *
#hello
mdev = mDEV()

server = udpServer(listen_ip="10.241.1.5", listen_port=6565, buffer_size=1024)

exitVal = False
recvData = [None,(None,None)]
#remote = ("10.241.1.3",7878)
def serRecv():
    global server, recvData, evitVal
    while True:

        recvData = server.recieve()
        if exitVal:
            return
    

recvThread = threading.Thread(target=serRecv, args=())
recvThread.daemon = True
recvThread.start()
x,y,rt,lt,xr,yr,rb,lb = 0, 0, 0, 0,0,0,0,0
#x - (-1,1)
#y - (-1,1)
#rt - (0,1)
#lt - (0)

try:

    while True:
        

        if recvData[0]:
            x,y,rt,lt,xr,yr,rb,lb = recvData[0].decode().split(",")
            x = float(x)
            y = float(y)
            rt = float(rt)
            lt = float(lt)
            xr = float(xr)
            yr = float(yr)
            rb= float(rb)
            lb= float(lb)

        speed = (rt - lt)*1000
        st_angle = 180 -(x +1)*90
        serv_x = 180 -(xr +1)*90
        ser_y = (yr +1)*90
        if (ser_y < 65):
            ser_y = 65
        #print(st_angle)
        mdev.move(speed,speed,st_angle)
        #print(serv_x)
        mdev.setServo('2', serv_x)
        mdev.setServo('3', ser_y)

        mdev.setBuzzer(rb*2000)
        server.send(str.encode(str(mdev.getSonic())))

        
except KeyboardInterrupt:
    print("Ending...")
        
while recvThread.is_alive():
    print(recvThread.is_alive())
    exitVal = True
    
print("killed")





