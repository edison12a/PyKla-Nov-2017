
# A very simple Flask Hello World app for you to get started with...

#from flask import Flask

#app = Flask(__name__)
#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import simi

app = Flask(__name__)

secret = "d331f932e0056f6c448ad2ee2e8706ecec8c99d2"
#bot = telepot.Bot('YOUR_AUTHORIZATION_TOKEN')
#bot.setWebhook("https://simisimi.pythonanywhere.com/{}".format(secret), max_connections=1)



app_id = "2002121170025563"
app_secret= "d67561c8827944d5821f83361f8c9448"
access_token = "EAAcc6ykiZCFsBALfC6cWlbcfbQbAe4xArFvyXLudGflZC5c8qDUc05Dqh14uXCkH7zAvatScrro2urhkifcdbuk413ZBDWocGPEsJsXjsothuMkZAM4nWBPZA3Wru97fCUw1fWhPNVlH7CVZBhEmzBaYwW2IYDX5Y08ntjwxI9qQZDZD"


ACCESS_TOKEN = access_token
VERIFY_TOKEN = "chan_knows_philip"


def reply(user_id, msg):

    msg = msg.lower()
    headers_Get = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    if 'weather' in msg:
        s = requests.Session()
        q = '+'.join(msg.split())
        url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
        r = s.get(url, headers=headers_Get)

        soup = BeautifulSoup(r.text, "html.parser")
        _NId = soup.find("div", {'class':'_NId'})
        for span in _NId.find_all("span"):
            msg = span.text.strip()
            break

    elif 'to ' in msg:
        s = requests.Session()
        q = '+'.join(msg.split())
        url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
        r = s.get(url, headers=headers_Get)

        soup = BeautifulSoup(r.text, "html.parser")
        _NId = soup.find("div", {'class':'_NId'})
        texts = []
        for span in _NId.find_all("span"):
            texts.append(span.text.strip())
        msg = texts[1]+' '+texts[2]

    elif msg.lower() == "hi":
        msg = 'Hi,\nMy name is chan'

    else:
        msg = "I Didn't catch that"

    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args['hub.verify_token'] == VERIFY_TOKEN:
        print("===========================================================================================================")
        return request.args['hub.challenge']
    else:
        return "Invalid verification token"


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    simi.xappend("chan_reqs.txt", data)
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
    #my_id = "1786791747998087"
    #reply(my_id, "Hi")




