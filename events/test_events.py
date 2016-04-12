import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_create_event():
    title = 'Lorem ipsum amet'
    json = {'title': title}
    url = BASE_URL + '/events'
    r = requests.post(url, json=json) 
    assert r.status_code == 201

def test_get_events_list():
    url = BASE_URL + '/events'
    r = requests.get(url) 
    assert r.status_code == 200
