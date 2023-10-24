import cv2
import numpy as np
import threading
from controllerHandler import XboxController
import time
from udpHandler import udpClient

client = udpClient(remote_ip="127.0.0.1",remote_port=20001, buffer_size=1024)
ps3 = XboxController()
exitVal = False
def updater():
    global ps3, exitVal, client
    while True:

        ps3.update()
        client.send(str.encode("hello"))
        if exitVal == True:
            break
    return
contUpdate = threading.Thread(target=updater,args=())
contUpdate.daemon = True
contUpdate.start()
h = int(640)
w = int(640)

lsx = 30
lsy = -30
rsx = 50
rsy = -30




ogImg = np.zeros((w, h, 3), dtype = np.uint8)
cv2.circle(ogImg, (int(w/4), int(h/4)), 90, (0,255,255), 2)
cv2.circle(ogImg, (int(w/4*3), int(h/4)), 90, (0,255,255), 2)

#cv2.circle(img, (int(w/4), int(h/4)), 5, (255,0,0), -1)
#cv2.circle(img, (int(w/4*3), int(h/4)), 5, (255,0,0), -1)


while True:
    
    img = cv2.line(ogImg, (int(w/4), int(h/4)), (int(w/4)+lsx, int(h/4)+lsy), (0,255,0), 10) 
    img = cv2.line(ogImg, (int(w/4*3), int(h/4)), (int(w/4*3)+rsx, int(h/4)+rsy), (0,255,0), 10) 

    cv2.circle(img, (int(w/4)+lsx, int(h/4)+lsy), 5, (255,0,0), -1)
    cv2.circle(img, (int(w/4*3+rsx), int(h/4)+rsy), 5, (255,0,0), -1)
    cv2.imshow("img",img)
    #exitVal = True
    #time.sleep(2)
    print(contUpdate.is_alive())
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

exitVal = True
cv2.destroyAllWindows()