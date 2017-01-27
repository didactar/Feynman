import requests
from conftest import session, URL_PREFIX
from feynman.users.utils.populate import populate_users


def test_list_post(session):
    raw_user = {
        'name': 'Carl Sagan',
        'avatar': 'carl-sagan'
    }
    r = requests.post(URL_PREFIX + 'users', json=raw_user)
    assert r.status_code == 201
    data = r.json()
    assert data['name'] == raw_user['name']
    assert data['avatar'] == raw_user['avatar']


def test_detail_delete(session):
    populate_users(1)
    users = requests.get(URL_PREFIX + 'users').json()['data']
    for user in users:
        user_detail_url = URL_PREFIX + 'users/' + user['username']
        assert requests.delete(user_detail_url).status_code == 204
        assert requests.delete(user_detail_url).status_code == 404


def test_get_unexisting_user(session):
    r = requests.get(URL_PREFIX + 'users/unexisting')
    assert r.status_code == 404


def test_detail_get(session):
    raw_user = {
        'name': 'Carl Sagan',
        'avatar': 'carl-sagan'
    }
    r = requests.post(URL_PREFIX + 'users', json=raw_user)
    username = r.json()['username']
    r = requests.get(URL_PREFIX + 'users/' + username)
    assert r.status_code == 200
    data = r.json() 
    assert data['name'] == raw_user['name']
    assert data['avatar'] == raw_user['avatar']


def test_get_users_list(session):
    populate_users(3)
    r = requests.get(URL_PREFIX + 'users')
    assert r.status_code == 200
    data = r.json()['data']
    assert len(data) == 3
