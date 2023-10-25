import cv2
import numpy as np
import threading
from controllerHandler import XboxController
import time
from udpHandler import udpClient
client = udpClient(remote_ip="10.241.1.4",remote_port=7878,buffer_size=1028)
ps3 = XboxController()
exitVal = False
radius = 90
lsx = 30
lsy = -30
rt = 50
lt = -30
carData = None
def updater():
    global ps3, exitVal, client, lsx, lsy, rt, lt
    while True:
        ps3.update()
        x = ps3.read()
        lsx = int(radius * float(x[0]))
        lsy = int(radius * float(x[1]))
        rt = float(x[2])
        lt = float(x[3])
        
        client.send(str.encode(','.join(x)))
        #carData = client.recieve()[0]
        #print('poo')
        if exitVal == True:
            return
    return

def wreciever():
    global carData
    while True:

        carData= client.recieve()
        #print("tried")
        if exitVal == True:
            return

contUpdate = threading.Thread(target=updater,args=())
contUpdate.daemon = True
contUpdate.start()
contRead = threading.Thread(target=wreciever,args=())
contRead.daemon = True
contRead.start()
h = int(640)
w = int(640)






ogImg = np.zeros((w, h, 3), dtype = np.uint8)
cv2.circle(ogImg, (int(w/4), int(h/4)), radius, (0,255,255), 2)
cv2.rectangle(ogImg, (int(w/4*3+30), int(h/4)-90),(int(w/4*3-30), int(h/4)+90), (255,0,0), 2)
cv2.rectangle(ogImg, (320, int(h/4)-90),(380, int(h/4)+90), (255,0,0), 2)
#cv2.circle(img, (int(w/4), int(h/4)), 5, (255,0,0), -1)
#cv2.circle(img, (int(w/4*3), int(h/4)), 5, (255,0,0), -1)


while True:
    img = ogImg.copy()
    img = cv2.line(img, (int(w/4), int(h/4)), (int(w/4)+lsx, int(h/4)-lsy), (0,255,0), 10) 
    #img = cv2.line(img, (int(w/4*3), int(h/4)), (int(w/4*3)+rsx, int(h/4)-rsy), (0,255,0), 10) 
    #carData= client.recieve()
    print(carData)
    cv2.circle(img, (int(w/4)+lsx, int(h/4)-lsy), 5, (255,0,0), -1)
    cv2.rectangle(img, (int(w/4*3+28), int(h/4)-int(88*(2*(rt-.5)))),(int(w/4*3-28), int(h/4)+88), (0,255,0), -1)
    cv2.rectangle(img, (322, int(h/4)-int(88*(2*(lt-.5)))),(378, int(h/4)+88), (0,255,0), -1)
    cv2.imshow("img",img[0:320, 0:640])
    #exitVal = True
    #time.sleep(2)
    
    if cv2.waitKey(1) == ord('q'):
        break

exitVal = True
time.sleep(.3)
print(contUpdate.is_alive())
print(contRead.is_alive())
cv2.destroyAllWindows()