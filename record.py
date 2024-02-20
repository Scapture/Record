import cv2


capGoalLine = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.57:554/stream1/out.h265")
capLeft = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.58:554/stream1/out.h265")
capRight = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.59:554/stream1/out.h265")

capGoalLine2 = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.14:554/stream1/out.h265")
capLeft2 = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.15:554/stream1/out.h265")
capRight2 = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.16:554/stream1/out.h265")

if(capGoalLine.isOpened()):
    print("GoalLine OK")
if(capLeft.isOpened()):
    print("Left OK")
if(capRight.isOpened()):
    print("Right OK")
if(capGoalLine2.isOpened()):
    print("GoalLine2 OK")
if(capLeft2.isOpened()):
    print("Left2 OK")
if(capRight2.isOpened()):
    print("Right2 OK")

# 영상 초기 설정, fps,width, height 값을 적절하게 맞추어야 함.
fourcc = cv2.VideoWriter_fourcc(*'X264')  # 비디오 코덱 설정
width = capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capGoalLine.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps= capGoalLine.get(cv2.CAP_PROP_FPS)

# 비디오 생성 객체 
outGoalLine = cv2.VideoWriter('output/goalline.mp4', fourcc, fps, (width, height))  # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정    
outLeft = cv2.VideoWriter('output/left.mp4', fourcc, fps, (width, height)) # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
outRight = cv2.VideoWriter('output/right.mp4', fourcc, fps, (width, height))

outGoalLine2 = cv2.VideoWriter('output/goalline.mp4', fourcc, fps, (width, height))
outLeft2 = cv2.VideoWriter('output/left.mp4', fourcc, fps, (width, height)) # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
outRight2 = cv2.VideoWriter('output/right.mp4', fourcc, fps, (width, height))
while True:
    # 프레임을 읽어옵니다.
    ret1, frame1 = capGoalLine.read()
    ret2, frame2 = capLeft.read()
    ret3, frame3 = capRight.read()

    ret4, frame4 = capGoalLine.read()
    ret5, frame5 = capLeft.read()
    ret6, frame6 = capRight.read()

    print(ret1, ", ", ret2, ", ", ret3)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 루프를 종료합니다.
        break
    if not ret1:
        print("Failed GoalLine.")
        break
    if not ret2:
        print("Failed left.")
        break
    if not ret3:
        print("Failed right.")
        break

    # 프레임을 화면에 표시합니다, 나중에 삭제 가능
    cv2.imshow('Webcam1 Recording', frame1)
    cv2.imshow('Webcam2 Recording', frame2)
    cv2.imshow('Webcam3 Recording', frame3)
    cv2.imshow('Webcam4 Recording', frame4)
    cv2.imshow('Webcam5 Recording', frame5)
    cv2.imshow('Webcam6 Recording', frame6)

    # 프레임을 녹화 파일에 추가합니다.
    outGoalLine.write(frame1)
    outLeft.write(frame2)
    outRight.write(frame3)
    outGoalLine2.write(frame4)
    outLeft2.write(frame5)
    outRight2.write(frame6)

outGoalLine.release()
outLeft.release()
outRight.release()
outGoalLine2.release()
outLeft2.release()
outRight2.release()

capGoalLine.release()
capLeft.release()
capRight.release()
capGoalLine2.release()
capLeft2.release()
capRight2.release()
