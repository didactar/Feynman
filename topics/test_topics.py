import requests
from slugify import slugify
import json
import os


BASE_URL = 'http://127.0.0.1:5000/api/v1/'

DATA_FILE = os.path.join(os.path.dirname(__file__), './test_topics_data.json')
with open(DATA_FILE) as data_file:    
    TOPICS = json.load(data_file)


class TestTopic:

    def test_create_topics(self):
        url = BASE_URL + 'topics'
        for topic in TOPICS:
            r = requests.post(url, json=topic) 
            assert r.status_code == 201

    def test_get_topics_list(self):
        url = BASE_URL + 'topics'
        r = requests.get(url) 
        data = json.loads(r.content.decode('utf-8'))
        assert len(data['data']) == len(TOPICS)
        assert r.status_code == 200

    def test_get_topic(self):
        for topic in TOPICS:
            slug = slugify(topic['name'], to_lower=True)
            url = BASE_URL + 'topics/' + slug
            r = requests.get(url) 
            data = json.loads(r.content.decode('utf-8'))
            assert r.status_code == 200
            assert data['slug'] == slug
            assert data['description'] == topic['description']

    def test_get_unexisting_topic(self):
        url = BASE_URL + 'topics/123abc123abc' 
        r = requests.get(url) 
        assert r.status_code == 404

    def test_delete_topic(self):
        for topic in TOPICS:
            slug = slugify(topic['name'], to_lower=True)
            url = BASE_URL + 'topics/' + slug
            assert requests.delete(url).status_code == 204
            assert requests.delete(url).status_code == 404
