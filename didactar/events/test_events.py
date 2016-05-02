
import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app


URL = BASE_URL + 'events'


@pytest.fixture(scope='module')
def setup_events():
    setup_test_app()


def test_create_get_delete_events(setup_events):

    with open('didactar/events/test_events_data.json') as f:
        EVENTS = json.load(f)

    # create events
    for event in EVENTS:
        r = requests.post(URL, json=event) 
        assert r.status_code == 201

    # get events list
    r = requests.get(URL) 
    assert r.status_code == 200

    # check events list length
    r_content = r.content.decode('utf-8')
    data = json.loads(r_content)
    assert len(data['data']) == len(EVENTS)

    # get event details
    for event in EVENTS:

        # check it exists
        slug = slugify(event['title'], to_lower=True)
        url = URL + '/' + slug
        r = requests.get(url) 
        assert r.status_code == 200

        # check correct data
        data = json.loads(r.content.decode('utf-8'))
        assert data['slug'] == slug
        assert data['description'] == event['description']

        # delete event
        assert requests.delete(url).status_code == 204
        assert requests.delete(url).status_code == 404
        

def test_get_unexisting_event():
    unexisting_event_slugs = ['aaa','bbb','ccc']
    for slug in unexisting_event_slugs:
        r = requests.get(URL + '/' + slug)
        assert r.status_code == 404
