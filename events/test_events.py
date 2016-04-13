import requests
from slugify import slugify
import json

BASE_URL = 'http://127.0.0.1:5000'

event_1 = {
    'title': 'Lorem ipsum',
    'description': 'This is an event about lorems ipsums'
}


def test_create_event():
    url = BASE_URL + '/events'
    r = requests.post(url, json=event_1) 
    assert r.status_code == 201

def test_get_events_list():
    url = BASE_URL + '/events'
    r = requests.get(url) 
    assert r.status_code == 200

def test_get_event():
    url = BASE_URL + '/events/' + slugify(event_1['title'], to_lower=True)
    r = requests.get(url) 
    assert r.status_code == 200
    data = json.loads(r.content.decode('utf-8'))
    assert data['slug'] == slugify(event_1['title'], to_lower=True)
    assert data['description'] == event_1['description']

def test_get_unexisting_event():
    url = BASE_URL + '/events/123abc123abc' 
    r = requests.get(url) 
    assert r.status_code == 404

def test_delete_event():
    url = BASE_URL + '/events/' + slugify(event_1['title'], to_lower=True)
    r = requests.delete(url) 
    assert r.status_code == 204
    r = requests.get(url) 
    assert r.status_code == 404
