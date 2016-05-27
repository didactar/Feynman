import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app

URL = BASE_URL + 'channels'


def populate_database():
    with open('didactar/users/test_users_data.json') as f:
        for user in json.load(f):
            requests.post(BASE_URL + 'users', json=user) 


@pytest.fixture(scope='module')
def setup_users():
    setup_test_app()
    populate_database()


def test_get_settings(setup_users):

    r = requests.get(BASE_URL + 'me/settings')
    assert r.status_code == 200

    data = json.loads(r.content.decode('utf-8'))
    assert 'id' in data
    assert 'name' in data
    assert 'username' in data
    assert 'avatar' in data
    assert 'about' in data
    assert 'language' in data
    assert 'timezone' in data
    assert 'email' in data
    assert 'emailFrequency' in data


def test_get_preferences(setup_users):

    r = requests.get(BASE_URL + 'me/preferences')
    assert r.status_code == 200

    data = json.loads(r.content.decode('utf-8'))
    assert 'name' in data
    assert 'username' in data
    assert 'avatar' in data
    assert 'language' in data
    assert 'timezone' in data
