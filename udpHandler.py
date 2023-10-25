import socket



class udpServer():
    def __init__(self,listen_ip="127.0.0.1",listen_port=20001,buffer_size=1024) -> None:
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPServerSocket.bind((listen_ip, listen_port))
        self.buffer_size = buffer_size
        self.packRecv = False
        self.addy = ('127.0.0.1', 9999)

    def send(self,data):
        #data is str.encode("hello")
        #address is ("127.0.0.1", 20001)
        self.UDPServerSocket.sendto(data, self.addy)

    def recieve(self):
        x = self.UDPServerSocket.recvfrom(self.buffer_size)
        if x and (len(x)>1):
            self.packRecv = True
            self.addy = x[1]

        return x



class udpClient():
    def __init__(self,remote_ip="127.0.0.1",remote_port=20001,buffer_size=1024) -> None:
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.buffer_size = buffer_size
        
    def send(self, data):
        #data is str.encode("hello")
        self.UDPClientSocket.sendto(data, (self.remote_ip,self.remote_port))
    def recieve(self):
        try:
            x = self.UDPClientSocket.recvfrom(self.buffer_size)
        except:
            x = False
        return x




