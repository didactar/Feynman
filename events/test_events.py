import requests
from slugify import slugify
import json
import os


BASE_URL = 'http://127.0.0.1:5000/api/v1/'

DATA_FILE = os.path.join(os.path.dirname(__file__), './test_events_data.json')
with open(DATA_FILE) as data_file:    
    EVENTS = json.load(data_file)


class TestEvent:

    def test_create_events(self):
        url = BASE_URL + 'events'
        for event in EVENTS:
            r = requests.post(url, json=event) 
            assert r.status_code == 201

    def test_get_events_list(self):
        url = BASE_URL + 'events'
        r = requests.get(url) 
        data = json.loads(r.content.decode('utf-8'))
        assert r.status_code == 200
        assert len(data['data']) == len(EVENTS)

    def test_get_event(self):
        for event in EVENTS:
            slug = slugify(event['title'], to_lower=True)
            url = BASE_URL + 'events/' + slug
            r = requests.get(url) 
            data = json.loads(r.content.decode('utf-8'))
            assert r.status_code == 200
            assert data['slug'] == slug
            assert data['description'] == event['description']

    def test_get_unexisting_event(self):
        url = BASE_URL + 'events/123abc123abc' 
        r = requests.get(url) 
        assert r.status_code == 404

    def test_delete_event(self):
        for event in EVENTS:
            slug = slugify(event['title'], to_lower=True)
            url = BASE_URL + 'events/' + slug
            assert requests.delete(url).status_code == 204
            assert requests.delete(url).status_code == 404
