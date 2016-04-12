import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_create():
    title = 'Lorem ipsum amet'
    json = {'title': title}
    url = BASE_URL + '/events'
    r = requests.post(url, json=json) 
    assert r.status_code == 201
