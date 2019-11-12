import requests
import json


def talk(content):
    url = 'http://www.tuling123.com/openapi/api'
    s = requests.session()
    d = {'key': 'b3f333bc09674b8986360293916bf84e', 'info': content}
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    return text['text']
