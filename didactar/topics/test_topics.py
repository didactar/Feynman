import pytest
import requests
from slugify import slugify
import json
import os

from didactar.database import db
from didactar import create_app
from didactar.config import TestConfig

from didactar.utils.shared_test_functions import BASE_URL


URL = BASE_URL + 'topics'

def load_json_file(json_file):
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path, json_file)
    with open(file_path) as f:
        return json.load(f)

TOPICS = load_json_file('test_topics_data.json')


@pytest.yield_fixture(scope="session")
def setup_topics():
    app = create_app(TestConfig)
    ctx = app.app_context()
    ctx.push()
    yield
    db.session.rollback()
    db.session.remove()


def test_create_get_delete_topics(setup_topics):

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
