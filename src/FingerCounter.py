import mediapipe as mp
import cv2
import time
import numpy as np
import serial


ser = serial.Serial('COM7', 115200)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils


webcam = cv2.VideoCapture()
webcam.open(0,cv2.CAP_DSHOW)
handsLM = mpHands.Hands(max_num_hands=2,min_detection_confidence=0.8,min_tracking_confidence=0.8)

status , frame = webcam.read()
imgH,imgW,imgC = frame.shape



tipIds=[4,8,12,16,20]

fps = 0
lastTotalFinger = -1
sekali = True
while True:
    status , frame = webcam.read()

    start = time.time()

    frame = cv2.flip(frame,1)
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    pr = handsLM.process(frame2)
    if pr.multi_hand_landmarks:    
        fingers=[]
        sekali = True
        for hand_landmarks in pr.multi_hand_landmarks:        
            hand = hand_landmarks
            mpDraw.draw_landmarks(frame,hand,mpHands.HAND_CONNECTIONS)
            landMarkList = []
            for id,landMark in enumerate(hand.landmark):
                xPos,yPos,zPos = int(landMark.x*imgW),int(landMark.y*imgH),int(landMark.z*imgW)
                landMarkList.append([id,xPos,yPos])    
            #Righ Hand
            if landMarkList[4][1] < landMarkList[17][1]:
                if landMarkList[tipIds[0]][1] < landMarkList[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            #Left Hand
            else:
                if landMarkList[tipIds[0]][1] > landMarkList[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            for id in range(1,5):
                if landMarkList[tipIds[id]][2] < landMarkList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        totalFinger = fingers.count(1) 
        if totalFinger != lastTotalFinger:
            lastTotalFinger = totalFinger
            if 0 < totalFinger < 10:
                ser.write(str(totalFinger).encode())
            else:
                ser.write(b'-')
    elif sekali:
       sekali = False
       lastTotalFinger = -1
       ser.write(b'-')
    end = time.time()
    totalTime = end - start
    if totalTime != 0 :
        fps = 1 / totalTime
    cv2.putText(frame, f'FPS: {int(fps)}', (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,255), 2)
    
    cv2.imshow("Finger Counter",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
webcam.release()
