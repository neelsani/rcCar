from udpHandler import udpServer
from mDev import mDEV

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
            break
    return
x,y,rt,lt = 0, 0, 0, 0
#x - (-1,1)
#y - (-1,1)
#rt - (0,1)
#lt - (0)

while True:

    if recvData[0]:
        x,y,rt,lt = str.decode(recvData[0]).split(",")

    speed = (rt - lt)*1000
    st_angle = (x +1)*90

