import paho.mqtt.client as mqtt
def run():
    # 변경
    broker_ip = "192.168.0.20" # 현재 이 컴퓨터를 브로커로 설정
    client = mqtt.Client()
    client.connect(broker_ip, 1883, 60)
    client.publish("convert", "start", qos=0)
    client.disconnect()


