import os


BASE_URL = 'http://127.0.0.1:5000/api/v1/'


def request_json(url):
    r = requests.get(url)
    c = r.content.decode('utf-8')
    return json.loads(c)
