from threading import Thread, Event
import cv2
import time

# 시작 시간이 달라서 영상 길이가 다른 버전
# imshow에서 싱크가 어느정도 맞음

# 전역 stop_event 생성
stop_event = Event()

class VideoStreamWidget(object):
    def __init__(self, src=0, output_file=None, window_name="Video Stream"):
        global stop_event
        self.capture = cv2.VideoCapture(src)
        self.output_file = output_file
        self.window_name = window_name
        self.stop_event = stop_event

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
        while not self.stop_event.is_set():
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
                self.stop_event.set()
                if self.output_file:
                    self.video_writer.release()
                self.capture.release()
                cv2.destroyAllWindows()

if __name__ == '__main__':
    video_stream_widgets = [
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.11:554/stream1/out.h265", output_file='output/goalline.mp4', window_name='Camera 1'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.12:554/stream1/out.h265", output_file='output/left.mp4', window_name='Camera 2'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.13:554/stream1/out.h265", output_file='output/right.mp4', window_name='Camera 3'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.14:554/stream1/out.h265", output_file='output/goalline2.mp4', window_name='Camera 4'),
        VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.15:554/stream1/out.h265", output_file='output/left2.mp4', window_name='Camera 5')
        # 다른 카메라 인스턴스화...
    ]
    # video_stream_widget1 = VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.11:554/stream1/out.h265", output_file='output/goalline.mp4', window_name='Camera 1')
    # video_stream_widget2 = VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.12:554/stream1/out.h265", output_file='output/left.mp4', window_name='Camera 2')
    # video_stream_widget3 = VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.13:554/stream1/out.h265", output_file='output/right.mp4', window_name='Camera 3')
    # video_stream_widget4 = VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.14:554/stream1/out.h265", output_file='output/goalline2.mp4', window_name='Camera 4')
    # video_stream_widget5 = VideoStreamWidget(src="rtsp://admin:asdf1346@@192.168.0.15:554/stream1/out.h265", output_file='output/left2.mp4', window_name='Camera 5')
    # 추가적인 카메라 인스턴스화...

    while True:
        try:
            if stop_event.is_set():
                break
            # video_stream_widget1.show_frame()
            # video_stream_widget2.show_frame()
            # video_stream_widget3.show_frame()
            # video_stream_widget4.show_frame()
            # video_stream_widget5.show_frame()
            for widget in video_stream_widgets:
                widget.show_frame()
            # 추가적인 카메라 프레임 표시...
        except AttributeError:
            pass
