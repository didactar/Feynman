import requests
from slugify import slugify
import json


BASE_URL = 'http://127.0.0.1:5000/api/v1/'

topic_1 = {
    'name': 'Biology',
    'description': 'This is a topic about biology'
}

topic_2 = {
    'name': 'Astronomy',
    'description': 'This is a topic about astronomy'
}

topic_3 = {
    'name': 'Science',
    'description': 'This is a topic about science'
}



class TestTopic:

    def test_create_topics(self):
        url = BASE_URL + 'topics'
        r = requests.post(url, json=topic_1) 
        assert r.status_code == 201
        r = requests.post(url, json=topic_2) 
        assert r.status_code == 201
        r = requests.post(url, json=topic_3) 
        assert r.status_code == 201

    def test_get_topics_list(self):
        url = BASE_URL + 'topics'
        r = requests.get(url) 
        data = json.loads(r.content.decode('utf-8'))
        assert len(data['data']) == 3
        assert r.status_code == 200

    def test_get_topic(self):
        url = BASE_URL + 'topics/' + slugify(topic_1['name'], to_lower=True)
        r = requests.get(url) 
        assert r.status_code == 200
        data = json.loads(r.content.decode('utf-8'))
        assert data['slug'] == slugify(topic_1['name'], to_lower=True)
        assert data['description'] == topic_1['description']

    def test_get_unexisting_topic(self):
        url = BASE_URL + 'topics/123abc123abc' 
        r = requests.get(url) 
        assert r.status_code == 404

    def test_delete_topic(self):
        url = BASE_URL + 'topics/' + slugify(topic_1['name'], to_lower=True)
        r = requests.delete(url) 
        assert r.status_code == 204
        r = requests.get(url) 
        assert r.status_code == 404
