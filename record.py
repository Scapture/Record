import cv2
import upload_file

# 녹화 시작 및 종료를 위한 상태 변환
recording = False

# mqtt_sub.py에서 녹화 종료를 위한 코드
def stop_recording():
    global recording
    recording = False

# mqtt_sub.py에서 녹화 시작을 위한 코드
def start_recording():
    global recording
    recording = True

def run():
    if recording:
        # 카메라 객체 생성, 변경
        capGoalLine = cv2.VideoCapture(4)  # 0은 기본 웹캠을 나타냅니다. 다른 웹캠을 사용하려면 적절한 인덱스를 사용하세요.
        capLeft = cv2.VideoCapture(0) 
        capRight = cv2.VideoCapture(2) 

        # capGoalLine.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # capGoalLine.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        # capGoalLine.set(cv2.CAP_PROP_FPS, 30)

        # capLeft.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # capLeft.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        # capLeft.set(cv2.CAP_PROP_FPS, 30)

        # capRight.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        # capRight.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        # capRight.set(cv2.CAP_PROP_FPS, 30)

        # 영상 초기 설정, fps,width, height 값을 적절하게 맞추어야 함.
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 비디오 코덱 설정
        fps = 30
        width = 1920
        height = 1080

        print("capGoalLine: ", capGoalLine.get(cv2.CAP_PROP_FPS), ", ", capGoalLine.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capGoalLine.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("capLeft: ", capLeft.get(cv2.CAP_PROP_FPS), ", ", capLeft.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capLeft.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print("capRight: ", capRight.get(cv2.CAP_PROP_FPS), ", ", capRight.get(cv2.CAP_PROP_FRAME_WIDTH), ", ", capRight.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 비디오 생성 객체 
        outGoalLine = cv2.VideoWriter('output/goalline.mp4', fourcc, fps, (width, height))  # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정    
        outLeft = cv2.VideoWriter('output/left.mp4', fourcc, fps, (width,height))  # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정
        outRight = cv2.VideoWriter('output/right.mp4', fourcc, fps, (width, height))  # 파일 이름, 코덱, 프레임 속도, 프레임 크기 설정

        while True:
            # 프레임을 읽어옵니다.
            ret1, frame1 = capGoalLine.read()
            ret2, frame2 = capLeft.read()
            ret3, frame3 = capRight.read()

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
            if not recording:
                print("record.py: stop")
                # cv2.destroyAllWindows()  # 모든 이미지 창을 닫습니다.
                break
        
            # 프레임을 화면에 표시합니다, 나중에 삭제 가능
            # cv2.imshow('Webcam1 Recording', frame1)
            # cv2.imshow('Webcam2 Recording', frame2)
            # cv2.imshow('Webcam3 Recording', frame3)

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
        upload_file.run()