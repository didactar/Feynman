import requests
from slugify import slugify
import json


BASE_URL = 'http://127.0.0.1:5000/api/v1/'

event_1 = {
    'title': 'Lorem ipsum',
    'description': 'This is an event about lorems ipsums'
}

event_2 = {
    'title': 'Lorem ipsum dolor sit amet',
    'description': 'This is an event about lorems ipsums dolors sits amets'
}

event_3 = {
    'title': 'I am the master of my fate',
    'description': 'I am the master of my soul'
}



class TestEvent:

    def test_create_events(self):
        url = BASE_URL + 'events'
        r = requests.post(url, json=event_1) 
        assert r.status_code == 201
        r = requests.post(url, json=event_2) 
        assert r.status_code == 201
        r = requests.post(url, json=event_3) 
        assert r.status_code == 201

    def test_get_events_list(self):
        url = BASE_URL + 'events'
        r = requests.get(url) 
        data = json.loads(r.content.decode('utf-8'))
        assert len(data['data']) == 3
        assert r.status_code == 200

    def test_get_event(self):
        url = BASE_URL + 'events/' + slugify(event_1['title'], to_lower=True)
        r = requests.get(url) 
        assert r.status_code == 200
        data = json.loads(r.content.decode('utf-8'))
        assert data['slug'] == slugify(event_1['title'], to_lower=True)
        assert data['description'] == event_1['description']

    def test_get_unexisting_event(self):
        url = BASE_URL + 'events/123abc123abc' 
        r = requests.get(url) 
        assert r.status_code == 404

    def test_delete_event(self):
        url = BASE_URL + 'events/' + slugify(event_1['title'], to_lower=True)
        r = requests.delete(url) 
        assert r.status_code == 204
        r = requests.get(url) 
        assert r.status_code == 404
