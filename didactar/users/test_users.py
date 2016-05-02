import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../')

import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app

URL = BASE_URL + 'users'


@pytest.fixture(scope='module')
def setup_users():
    setup_test_app()


def test_create_get_delete_users(setup_users):

    with open('didactar/users/test_users_data.json') as f:
        USERS = json.load(f)

    # create items
    for user in USERS:
        r = requests.post(URL, json=user) 
        assert r.status_code == 201

    # get list
    r = requests.get(URL) 
    assert r.status_code == 200

    # check list length
    r_content = r.content.decode('utf-8')
    data = json.loads(r_content)
    assert len(data['data']) == len(USERS)

    # get details
    for user in USERS:

        # check it exists
        username = slugify(user['name'], to_lower=True)
        url = URL + '/' + username
        r = requests.get(url) 
        assert r.status_code == 200

        # check correct data
        data = json.loads(r.content.decode('utf-8'))
        assert data['username'] == username
        assert data['avatar'] == user['avatar']

        # delete item
        assert requests.delete(url).status_code == 204
        assert requests.delete(url).status_code == 404
        

def test_get_unexisting_user():
    unexisting_usernames = ['aaa','bbb','ccc']
    for username in unexisting_usernames:
        r = requests.get(URL + '/' + username)
        assert r.status_code == 404
