import requests
from flask import url_for
from fixtures import session, app
from .populate import populate_topics


def test_list_post(session):
    raw_topic = {
        'name': 'Astronomy',
        'description': 'Description of the topic Astronomy',
        'image': 'astronomy.jpg'
    }
    topic_list_url = url_for('topics.topic_list')
    r = requests.post(topic_list_url, json=raw_topic)
    assert r.status_code == 201
    data = r.json()
    assert data['name'] == raw_topic['name']
    assert data['description'] == raw_topic['description']
    assert data['image'] == raw_topic['image']


def test_detail_delete(session):
    populate_topics(1)
    topic_list_url = url_for('topics.topic_list')
    topics = requests.get(topic_list_url).json()['data']
    for topic in topics:
        topic_detail_url = url_for('topics.topic_detail', topic_slug=topic['slug'])
        assert requests.delete(topic_detail_url).status_code == 204
        assert requests.delete(topic_detail_url).status_code == 404


def test_get_unexisting_topic(session):
    topic_detail_url = url_for('topics.topic_detail', topic_slug='unexisting_slug')
    assert requests.get(topic_detail_url).status_code == 404


def test_detail_get(session):
    raw_topic = {
        'name': 'Astronomy',
        'description': 'Description of the topic Astronomy',
        'image': 'astronomy.jpg'
    }
    topic_list_url = url_for('topics.topic_list')
    r = requests.post(topic_list_url, json=raw_topic)
    topic_slug = r.json()['slug']
    topic_detail_url = url_for('topics.topic_detail', topic_slug=topic_slug)
    r = requests.get(topic_detail_url)
    assert r.status_code == 200
    data = r.json() 
    assert data['name'] == raw_topic['name']
    assert data['description'] == raw_topic['description']
    assert data['image'] == raw_topic['image']


def test_get_topics_list(session):
    populate_topics(3)
    topic_list_url = url_for('topics.topic_list')
    r = requests.get(topic_list_url)
    assert r.status_code == 200
    data = r.json()['data']
    assert len(data) == 3
