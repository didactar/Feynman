import requests
from slugify import slugify

BASE_URL = 'http://127.0.0.1:5000'

title = 'Lorem ipsum'

def test_create_event():
    json = {'title': title}
    url = BASE_URL + '/events'
    r = requests.post(url, json=json) 
    assert r.status_code == 201

def test_get_events_list():
    url = BASE_URL + '/events'
    r = requests.get(url) 
    assert r.status_code == 200

def test_get_event():
    url = BASE_URL + '/events/' + slugify(title, to_lower=True)
    r = requests.get(url) 
    assert r.status_code == 200

def test_get_unexisting_event():
    url = BASE_URL + '/events/123abc123abc' 
    r = requests.get(url) 
    assert r.status_code == 404

def test_delete_event():
    url = BASE_URL + '/events/' + slugify(title, to_lower=True)
    r = requests.delete(url) 
    assert r.status_code == 204
    r = requests.get(url) 
    assert r.status_code == 404
