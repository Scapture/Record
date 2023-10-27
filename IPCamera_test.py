import cv2 as cv
import sys

#rtsp: Real Time Stream Protocol
cap = cv.VideoCapture("rtsp://admin:zxcv1346@192.168.0.31:554/stream1/out.h265")

while(1):
    ret, frame = cap.read()
    
    if ret == False:
        print("프레임을 읽어 오지 못했습니다.")
        break;
    else:    
        cv.imshow('VIDEO', frame)
        if cv.waitKey(1) == 113: #'q' 키 누를 때 종료 (아스키 코드 값 113)
            break
    
cap.release()
cv.destroyAllWindows()
        
