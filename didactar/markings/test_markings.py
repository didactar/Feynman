import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app


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
            list_url = BASE_URL + 'events/' + event['slug'] + '/topics'
            r = requests.post(list_url, json=topic)
            assert r.status_code == 201

    # check all topics for each event    
    for event in events:
        topic_list_url = BASE_URL + 'events/' + event['slug'] + '/topics'
        r = requests.get(topic_list_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        event_topics = json.loads(request_content)['data']
        assert len(event_topics) == len(topics)    


    # check all events for each topic    
    for topic in topics:
        event_list_url = BASE_URL + 'topics/' + topic['slug'] + '/events'
        r = requests.get(event_list_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        topic_events = json.loads(request_content)['data']
        assert len(topic_events) == len(events)    


    # delete each topic from each event
    for event in events:
        for topic in topics:
            detail_url = BASE_URL + 'events/' + event['slug'] + '/topics/' + topic['slug']
            assert requests.delete(detail_url).status_code == 204
            assert requests.delete(detail_url).status_code == 404
