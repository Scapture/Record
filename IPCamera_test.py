import cv2 as cv
import sys

#rtsp: Real Time Stream Protocol
cap = cv.VideoCapture("rtsp://admin:asdf1346@@192.168.0.57:554/stream1/out.h265")
cap2 = cv.VideoCapture("rtsp://admin:asdf1346@@192.168.0.58:554/stream1/out.h265")

while(1):
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    
    if ret == False and ret2 == False:
        print("프레임을 읽어 오지 못했습니다.")
        break
    else:    
        cv.imshow('VIDEO', frame)
        cv.imshow('VIDEO2', frame2)
        if cv.waitKey(1) == 113: #'q' 키 누를 때 종료 (아스키 코드 값 113)
            break
    
cap.release()
cv.destroyAllWindows()
        
