import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    global msg
    msg = str(message.payload.decode("utf-8"))


global msg
msg = ''
addr = 'broker.emqx.io'
port = 1883

client = mqtt.Client('Broker')
client.on_message = on_message
client.connect(addr, port=port)

command = input('Start bruteforce? y/n')

if (command == 'y'):
    client.publish('topic/hack', 'start')
while True:
    client.loop_start()
    client.subscribe('topic/worker/result')
    client.loop_stop()
    time.sleep(1)

    if ('Success' in msg):
        client.publish('topic/hack', 'stop')
        print(msg)
        break
    elif('Failed' in msg):
        print('something went wrong')
        break
