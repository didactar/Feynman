import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import create_test_app


URL = BASE_URL + 'topics'


def populate_database():

    with open('didactar/events/test_events_data.json') as f:
        EVENTS = json.load(f)
    for event in EVENTS:
        requests.post(BASE_URL + 'events', json=event) 

    with open('didactar/topics/test_topics_data.json') as f:
        TOPICS = json.load(f)
    for topic in TOPICS:
        requests.post(BASE_URL + 'topics', json=topic) 



@pytest.fixture(scope='module')
def setup_events_topics():
    create_test_app()
    populate_database()



def test_create_get_delete_events_topics(setup_events_topics):

    # get existing events and topics
    
    events_request = requests.get(BASE_URL + 'events')
    events_content = events_request.content.decode('utf-8')
    events = json.loads(events_content)['data']
    assert len(events)

    topics_request = requests.get(BASE_URL + 'topics')
    topics_content = topics_request.content.decode('utf-8')
    topics = json.loads(topics_content)['data']
    assert len(topics)

    for event in events:
        for topic in topics:

            # create each topic for each event
            list_url = BASE_URL + 'events/' + event['slug'] + '/topics'
            r = requests.post(list_url, json=topic)
            assert r.status_code == 201

            # get detail
            detail_url = BASE_URL + 'events/' + event['slug'] + '/topics/' + topic['slug']
            r = requests.get(detail_url)
            assert r.status_code == 200
            
            # check correct data
            request_content = r.content.decode('utf-8')
            data = json.loads(request_content)
            assert data['event']['id'] == event['id']
            assert data['topic']['id'] == topic['id']

            # delete each topic from each event
            assert requests.delete(detail_url).status_code == 204
            assert requests.delete(detail_url).status_code == 404
