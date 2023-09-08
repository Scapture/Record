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
