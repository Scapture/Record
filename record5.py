from threading import Thread, Event
import cv2
import time

# 시작 시간을 같게 설정 영상 길이가 같은 버전
# imshow에서 싱크가 맞지 않음

# 전역 시작 및 종료 이벤트 생성
start_event = Event()
stop_event = Event()

class VideoStreamWidget(object):
    def __init__(self, src=0, output_file=None, window_name="Video Stream"):
        self.capture = cv2.VideoCapture(src)
        self.output_file = output_file
        self.window_name = window_name

        if output_file:
            fourcc = cv2.VideoWriter_fourcc(*'X264')
            fps = self.capture.get(cv2.CAP_PROP_FPS)
            self.delay = max(1, int(1000 / fps))  # 프레임 사이의 대기 시간(ms) 계산
            width, height = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.video_writer = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        start_event.wait()  # 시작 이벤트가 설정될 때까지 대기
        while not stop_event.is_set():
            if self.capture.isOpened():
                ret, frame = self.capture.read()
                if ret:
                    self.frame = frame
                    if self.output_file:
                        self.video_writer.write(self.frame)
                else:
                    print("Frame read failed")
                    break
            # time.sleep(self.delay / 1000.0)  # 프레임 처리 속도 조절
            time.sleep(0.01)

    def show_frame(self):
        if hasattr(self, 'frame'):
            cv2.imshow(self.window_name, self.frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                stop_event.set()
                if self.output_file:
                    self.video_writer.release()
                self.capture.release()
                cv2.destroyAllWindows()

if __name__ == '__main__':
    # 카메라 인스턴스화
    video_stream_widgets = [
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.11:554/stream1/out.h265", output_file='output/goalline.mp4', window_name='Camera 1'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.12:554/stream1/out.h265", output_file='output/left.mp4', window_name='Camera 2'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.13:554/stream1/out.h265", output_file='output/right.mp4', window_name='Camera 3'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.14:554/stream1/out.h265", output_file='output/goalline2.mp4', window_name='Camera 4'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.15:554/stream1/out.h265", output_file='output/left2.mp4', window_name='Camera 5')
    ]
    start_event.set()  # 모든 스트림의 캡처 시작 신호 보내기

    while True:
        try:
            if stop_event.is_set():
                break
            for widget in video_stream_widgets:
                widget.show_frame()
        except AttributeError:
            pass
