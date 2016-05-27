import json
import requests
import sys
import key


def send(conv_id, msg):
    url = 'https://api.pushbullet.com/v2/ephemerals'

    headers = {
        'Access-Token': key.api_key,
        'Content-Type': 'application/json'
    }

    data = {
        "push": {
            "conversation_iden": conv_id,
            "message": msg,
            "source_user_iden": "ujviXQ0TMZ",
            "package_name": "com.pushbullet.android",
            "source_user_iden": "ujviXQ0TMZ",
            "target_device_iden": "ujviXQ0TMZ2sjAiNWhbZ12",
            "type": "messaging_extension_reply"
        },
        "type": "push"
    }

    resp = requests.post(url, data=json.dumps(data), headers=headers)

    if resp.json() == '{}':
        print('Sent successfully!')

    else:
        print(resp.json())


def get_number(name):
    contacts = [('Me', 15167430940)]
 
    return dict(contacts)[name]


try:
    send(get_number(sys.argv[1]), sys.argv[2])
except:
    print("Usage: 'sms NAME MESSAGE'")
