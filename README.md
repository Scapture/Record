# Raspberry-PI
풋살 영상 촬영을 위한 SW(Raspberry PI)

## 네트워크 구성
### MQTT Broker, FTP Server
GPU Computer에서 수행 
### 모든 기기 로컬 네트워크에서 구동 가정

## MQTT
### Client -> RaspberryPI
Topic: record
message: start(녹화 시작), end(녹화 종료 및 영상 FTP로 전달)

### RaspberryPI -> GPU Computer
Topic: convert
message: start(하이라이트 영상 추출 시작)


## 환경 구성
### FTP
#### upload_file.py
FTP Server IP 수정(고정 IP가 아니기에 그때마다 확인하고 수정)
FTP id, pw(현재 내가 만들어놓은걸로 해놨음, 이거 바꿔야 됨)
전송할 파일 디렉토리(Raspberry PI에 맞게)
전송받을 디렉토리 주소 수정(GPU Computer에 영상이 들어갈 위치 확인하고 그곳으로 변경)


### MQTT
#### mqtt.pub.py
broker_ip를 GPU Computer의 ip로 변경
#### mqtt.sub.py
위와 동일

### 카메라 설정
#### record.py
카메라 번호 인덱스를 0,1,2로 해놓은 상태.
-> Raspberry PI에 연결된 카메라 인덱스에 맞게 수정