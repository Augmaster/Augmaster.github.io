import cv2 as cv2
import mediapipe as mp
import time
import math
import osascript
import numpy as np

from modules import handTracking as htm

previous_time = 0
current_time = 0

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

minVol = 0
maxVol = 100

hand_detector = htm.handDetector(detection_confidence=0.7)

while True:
    success, img = cap.read()
    img = hand_detector.find_hands(img)
    lm_list = hand_detector.find_position(img, False)
    
    if len(lm_list) != 0:
        
        x1, y1 = lm_list[4][1:]
        x2, y2 = lm_list[8][1:]
                
        cv2.circle(img, (x1, y1), 5, (0,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (0,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
        
        lenght = math.hypot(x2-x1, y2-y1)
        vol = np.interp(lenght, [0, 120], [minVol, maxVol])
        print(vol)
        osascript.osascript("set volume output volume {}".format(vol))
           
    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time
    
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) == ord('q'):
        break
