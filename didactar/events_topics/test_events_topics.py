import requests
from slugify import slugify
import json
import os


BASE_URL = 'http://127.0.0.1:5000/api/v1/'

EVENTS_FILE = os.path.join(os.path.dirname(__file__), '../events/test_events_data.json')
with open(EVENTS_FILE) as data_file:    
    EVENTS = json.load(data_file)

TOPICS_FILE = os.path.join(os.path.dirname(__file__), '../topics/test_topics_data.json')
with open(TOPICS_FILE) as data_file:    
    TOPICS = json.load(data_file)


def request_json(url):
    r = requests.get(url)
    c = r.content.decode('utf-8')
    return json.loads(c)


def create_events():
    url = BASE_URL + 'events'
    for event in EVENTS:
        r = requests.post(url, json=event) 

def delete_events():
    for event in self.events:
        url = BASE_URL + 'events/' + event.slug
        requests.delete(url)

def create_topics():
    url = BASE_URL + 'topics'
    for topic in TOPICS:
        r = requests.post(url, json=topic) 

def delete_topics():
    for topic in self.topics:
        url = BASE_URL + 'topics/' + topic.slug
        requests.delete(url)




class TestEventTopics:

    def setup_class(self):
        create_events()
        create_topics()
        self.topics = request_json(BASE_URL + 'topics')
        self.events = request_json(BASE_URL + 'events')

    def test_create_event_topic(self):
        for event in self.events:
            for topic in self.topics:
                url = BASE_URL + 'events/' + event.slug + '/topics'
                r = requests.post(url, json=topic).status
                assert r.status_code == 201

    def teardown_class(self):
        delete_events()
        delete_topics()
