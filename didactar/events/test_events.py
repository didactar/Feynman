import requests
from slugify import slugify
import json
import os

from .models import Event

URL = 'http://127.0.0.1:5000/api/v1/events'

DATA_FILE = os.path.join(os.path.dirname(__file__), './test_events_data.json')
with open(DATA_FILE) as data_file:    
    EVENTS = json.load(data_file)


class TestEvent:


    def test_create_get_delete_events(self):
    
        # create events
        for event in EVENTS:
            r = requests.post(URL, json=event) 
            assert r.status_code == 201

        # get events list
        r = requests.get(URL) 
        assert r.status_code == 200

        # check events list length
        data = json.loads(r.content.decode('utf-8'))
        assert len(data['data']) == len(EVENTS)

        # check events list contents
        for event in EVENTS:
            assert event in data
        
        # get event details
        for event in EVENTS:

            # check it exists
            slug = slugify(event['title'], to_lower=True)
            r = requests.get(URL + '/' + slug) 
            assert r.status_code == 200

            # check correct data
            data = json.loads(r.content.decode('utf-8'))
            assert data['slug'] == slug
            assert data['description'] == event['description']

            # delete event
            assert requests.delete(url).status_code == 204

            # try to delete again
            assert requests.delete(url).status_code == 404
            

    def test_get_unexisting_event(self):
        unexisting_event_slugs = ['aaa','bbb','ccc']
        for slug in unexisting_event_slugs:
            r = requests.get(URL + '/' + slug)
            assert r.status_code == 404

    def teardown_class(cls):
        events = Event.query.all()
        for event in events:
            event.delete()
