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

    topics_request = requests.get(BASE_URL + 'topics')
    topics_content = topics_request.content.decode('utf-8')
    topics = json.loads(topics_content)['data']


    # add each topic to each event
    '''
    for event in events:
        for topic in topics:
            url = BASE_URL + 'events/' + event.slug + '/topics'
            r = requests.post(url, json=topic)
            assert r.status_code == 201
        '''
