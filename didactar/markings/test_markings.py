import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../')

import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app


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
def setup_markings():
    setup_test_app()
    populate_database()


def test_create_get_delete_markings(setup_markings):

    # get existing events and topics
    
    events_request = requests.get(BASE_URL + 'events')
    events_content = events_request.content.decode('utf-8')
    events = json.loads(events_content)['data']
    assert len(events)

    topics_request = requests.get(BASE_URL + 'topics')
    topics_content = topics_request.content.decode('utf-8')
    topics = json.loads(topics_content)['data']
    assert len(topics)

    # create each topic for each event
    for event in events:
        for topic in topics:
            list_url = BASE_URL + 'markings'
            data = {'event': event, 'topic': topic}
            r = requests.post(list_url, json=data)
            assert r.status_code == 201

    # check all topics for each event    
    for event in events:
        event_markings_url = BASE_URL + 'events/' + event['slug'] + '/markings'
        r = requests.get(event_markings_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        event_markings = json.loads(request_content)['data']
        assert len(event_markings) == len(topics)    

    # check all events for each topic    
    for topic in topics:
        topic_markings_url = BASE_URL + 'topics/' + topic['slug'] + '/markings'
        r = requests.get(topic_markings_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        topic_markings = json.loads(request_content)['data']
        assert len(topic_markings) == len(events)

    # delete all markings
    for event in events:
        event_markings = BASE_URL + 'events/' + event['slug'] + '/markings'
        r = requests.get(event_markings)
        request_content = r.content.decode('utf-8')
        markings = json.loads(request_content)['data']
        for m in markings:
            marking_detail_url = '{}markings/{}'.format(BASE_URL, m['id'])
            assert requests.delete(marking_detail_url).status_code == 204
            assert requests.delete(marking_detail_url).status_code == 404
