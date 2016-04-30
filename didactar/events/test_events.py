import pytest
import requests
from slugify import slugify
import json
import os

from didactar.database import db
from didactar import create_app
from didactar.config import TestConfig

from didactar.utils.shared_test_functions import BASE_URL


URL = BASE_URL + 'events'

def load_json_file(json_file):
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, json_file)
    with open(file_path) as f:
        return json.load(f)

EVENTS = load_json_file('test_events_data.json')


@pytest.yield_fixture(scope="module")
def setup_events():
    app = create_app(TestConfig)
    ctx = app.app_context()
    ctx.push()
    yield
    db.session.rollback()
    db.session.remove()


def test_create_get_delete_events(setup_events):

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
