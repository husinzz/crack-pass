import paho.mqtt.client as mqtt

addr = 'localhost'
port = 9000

client = mqtt.Client('Worker')
client.connect(addr, port=port)

client.publish('topic/worker/1', 'Worker 1 active')
client.publish('topic/worker/2', 'Worker 2 active')
client.publish('topic/worker/result', 'Password is found, "Password"')
