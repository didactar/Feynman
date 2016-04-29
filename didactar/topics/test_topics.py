import requests
from slugify import slugify
import json
import os

#from shared_test_functions import BASE_URL
#from shared_test_functions import request_json

from didactar.events.models import Event


DATA_FILE = os.path.join(os.path.dirname(__file__), './test_topics_data.json')
with open(DATA_FILE) as data_file:    
    TOPICS = json.load(data_file)


class TestTopic:
    
    def setup_class(cls):
        url = BASE_URL + 'topics'
        for topic in TOPICS:
            r = requests.post(url, json=topic) 

    def test_create_topic(self):
        new_topics = [
            {
            "name": "Mathematics",
            "description": "This is a topic about mathematics"
            }
        ]
        url = BASE_URL + 'topics'
        existing_topics = request_json(url)
        for topic in new_topics:
            r = requests.post(url, json=topic) 
            assert r.status_code == 201

    def test_get_topic(self):
        for topic in TOPICS:
            slug = slugify(topic['name'], to_lower=True)
            url = BASE_URL + 'topics/' + slug
            r = requests.get(url) 
            assert r.status_code == 200
            data = json.loads(r.content.decode('utf-8'))
            assert data['slug'] == slug
            assert data['description'] == topic['description']

    def test_get_unexisting_topic(self):
        url = BASE_URL + 'topics/123abc123abc' 
        assert requests.get(url).status_code == 404

    def test_delete_topic(self):
        for topic in TOPICS:
            slug = slugify(topic['name'], to_lower=True)
            url = BASE_URL + 'topics/' + slug
            assert requests.delete(url).status_code == 204
            assert requests.delete(url).status_code == 404

    def teardow_class(cls):
        topics = request_json(BASE_URL + 'topics')
        for topic in topics:
            url = BASE_URL + 'topics/' + topic.slug
            requests.delete(url)
