import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput import keyboard
from pynput.keyboard import Controller
from time import sleep
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

keyboard = Controller()

detector = HandDetector(detectionCon = 0.8, maxHands=2)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    
    cv2.rectangle(img,(600,100),(700,200),(255,0,255), cv2.FILLED)
    cv2.putText(img, "^",(605,195),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),3)

    cv2.rectangle(img,(600,220),(700,320),(255,0,255), cv2.FILLED)
    cv2.putText(img, "v",(605,295),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),3)

    cv2.rectangle(img,(725,175),(825,275),(255,0,255), cv2.FILLED)
    cv2.putText(img, ">",(750,235),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),3)
    
    cv2.rectangle(img,(475,175),(575,275),(255,0,255), cv2.FILLED)
    cv2.putText(img, "<",(500,235),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),3)

    if lmList:
        x1up, y1up = 600, 100  
        x2up, y2up = 700, 200
        x1down, y1down = 600, 220
        x2down, y2down = 700, 320
        x1right, y1right = 725, 175
        x2right, y2right = 825, 275
        x1left, y1left = 475, 175
        x2left, y2left = 575, 275
        if x1up < lmList[8][0] < x2up and y1up < lmList[8][1] < y2up:
            
            keyboard.press("w")
            sleep(2)

        elif x1down < lmList[8][0] < x2down and y1up < lmList[8][1] < y2down:
            
            keyboard.press("s")
            sleep(2)

        elif x1right < lmList[8][0] < x2right and y1right < lmList[8][1] < y2right:
            
            keyboard.press("d")
            sleep(2)

        elif x1left < lmList[8][0] < x2left and y1left < lmList[8][1] < y2left:
            
            cv2.rectangle(img,(475,175),(575,275),(0,255,0), cv2.FILLED)
            keyboard.press("a")
            sleep(2)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
  