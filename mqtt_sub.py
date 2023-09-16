import paho.mqtt.client as mqtt_client
import record
import threading

# 변경
mqtt_broker = "192.168.0.4"
topic = "record"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print("arrived: ", message)

    if message == "start":
        record.start_recording()
        print("Start recording")

    elif message == "end":
        record.stop_recording()
        print("Stop recording")

client = mqtt_client.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker, 1883, 60)

# 별도의 스레드에서 MQTT 메시지 수신을 처리합니다.
def mqtt_thread():
    client.loop_forever()

mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.daemon = True
mqtt_thread.start()

# 메인 스레드에서 녹화 루프를 실행합니다.
while True:
    record.run()