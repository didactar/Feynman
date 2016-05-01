import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app


URL = BASE_URL + 'topics'


@pytest.fixture(scope='module')
def setup_topics():
    setup_test_app()


def test_create_get_delete_topics(setup_topics):

    with open('didactar/topics/test_topics_data.json') as f:
        TOPICS = json.load(f)

    # create topics
    for topic in TOPICS:
        r = requests.post(URL, json=topic) 
        assert r.status_code == 201

    # get topics list
    r = requests.get(URL) 
    assert r.status_code == 200

    # check topics list length
    r_content = r.content.decode('utf-8')
    data = json.loads(r_content)
    assert len(data['data']) == len(TOPICS)

    # get topic details
    for topic in TOPICS:

        # check it exists
        slug = slugify(topic['name'], to_lower=True)
        url = URL + '/' + slug
        r = requests.get(url) 
        assert r.status_code == 200

        # check correct data
        data = json.loads(r.content.decode('utf-8'))
        assert data['slug'] == slug
        assert data['description'] == topic['description']

        # delete topic
        assert requests.delete(url).status_code == 204
        assert requests.delete(url).status_code == 404
        

def test_get_unexisting_topic():
    unexisting_topic_slugs = ['aaa','bbb','ccc']
    for slug in unexisting_topic_slugs:
        r = requests.get(URL + '/' + slug)
        assert r.status_code == 404
