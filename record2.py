import cv2

capGoalLine = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.57:554/stream1/out.h265")
capLeft = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.58:554/stream1/out.h265")
capRight = cv2.VideoCapture("rtsp://admin:asdf1346@@192.168.0.59:554/stream1/out.h265")

if(capGoalLine.isOpened()):
    print("GoalLine OK")
if(capLeft.isOpened()):
    print("Left OK")
if(capRight.isOpened()):
    print("Right OK")

# capGoalLine.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# capGoalLine.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# capGoalLine.set(cv2.CAP_PROP_FPS, 24
# capLeft.set(cv2.CAP_PROP_FPS, 24)
# capLeft.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# capLeft.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080
# capRight.set(cv2.CAP_PROP_FPS, 24)
# capRight.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# capRight.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080
# 영상 초기 설정, fps,width, height 값을 적절하게 맞추어야 함.
# fourcc = cv2.VideoWriter_fourcc(*'X264')  # 비디오 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
width = capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capGoalLine.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps= capGoalLine.get(cv2.CAP_PROP_FPS)

print("capGoalLine: ", capGoalLine.get(cv2.CAP_PROP_FPS), ", ", capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capGoalLine.get(cv2. CAP_PROP_FRAME_HEIGHT))
print("capLeft: ", capLeft.get(cv2.CAP_PROP_FPS), ", ", capLeft.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capLeft.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("capRight: ", capRight.get(cv2.CAP_PROP_FPS), ", ", capRight.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capRight.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 비디오 생성 객체 
# outGoalLine = cv2.VideoWriter('output/goalline.mp4', fourcc, int(fps)*0.8, (int(width), int(height)))  # 파일 이름, 코덱, 프레임 속도프레임 크기 설정    
# outLeft = cv2.VideoWriter('output/left.mp4', fourcc, int(fps)*0.8, (int(width), int(height)))  # 파일 이름, 코덱, 프레임 속도, 프레임 크설정
# outRight = cv2.VideoWriter('output/right.mp4', fourcc, int(fps)*0.8, (int(width), int(height)))  # 파일 이름, 코덱, 프레임 속도, 프레임 크설
outGoalLine = cv2.VideoWriter('output/goalline.mp4', fourcc, fps, (int(width), int(height)))  # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정    
outLeft = cv2.VideoWriter('output/left.mp4', fourcc, fps, (int(width), int(height))) # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
outRight = cv2.VideoWriter('output/right.mp4', fourcc, fps, (int(width), int(height)))


while True:
    # 프레임을 읽어옵니다.
    ret1, frame1 = capGoalLine.read()
    ret2, frame2 = capLeft.read()
    ret3, frame3 = capRight.read()
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
    # stop_recording() 을 통해 recording이 False가 되면 종료
    # if not recording:
    #     print("record.py: stop")
    #     cv2.destroyAllWindows()  # 모든 이미지 창을 닫습니다.
    #     break

    # 프레임을 화면에 표시합니다, 나중에 삭제 가능
    cv2.imshow('Webcam1 Recording', frame1)
    cv2.imshow('Webcam2 Recording', frame2)
    cv2.imshow('Webcam3 Recording', frame3)
    # 프레임을 녹화 파일에 추가합니다.
    outGoalLine.write(frame1)
    outLeft.write(frame2)
    outRight.write(frame3)

outGoalLine.release()
outLeft.release()
outRight.release()
capGoalLine.release()
capLeft.release()
capRight.release()
# FTP 파일 전송
# upload_file.run()