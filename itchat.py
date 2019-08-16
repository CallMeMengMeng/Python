#coding=utf8
import requests
import itchat

KEY = '0c038527a42a49bf8c4ed084437294e5'

def get_response(msg):
    Url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'pth-robot',
    }
    try:
        r = requests.post(Url, data=data).json()
        return r.get('text')
    except:
        return

#@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
