from udpHandler import udpClient


client = udpClient()
while True:
    client.send(str.encode("rt"))