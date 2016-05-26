import json
import subprocess
import websocket
import api_key

def notify(message):
    subprocess.call("/home/matthunz/bin/notify.sh '%s'" % message, shell=True)


def on_open(ws):
    try:
        ws.send('Hello World')
        print('Connection established')
    except:
        print('Connection failed')


def on_message(ws, message):
    message = json.loads(message)

    try:
        info = message['push']['notifications'][0]
        notify("%%{F'#586ca7'} %%{F'#aaaaaa'} %s: %s" % (info['title'], info['body']))
    except: None

ws = websocket.WebSocketApp('wss://stream.pushbullet.com/websocket/%s' % api_key,
                            on_message = on_message)

ws.on_open = on_open
ws.run_forever()
