from udpHandler import udpClient


client = udpClient(remote_ip="10.241.1.4",remote_port=7878, buffer_size=1024)

client.send(str.encode("rt"))
