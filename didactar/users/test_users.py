import requests
from flask import url_for
from fixtures import session, app
from .populate import populate_users


def test_list_post(session):
    raw_user = {
        'name': 'Carl Sagan',
        'avatar': 'carl-sagan'
    }
    user_list_url = url_for('users.user_list')
    r = requests.post(user_list_url, json=raw_user)
    assert r.status_code == 201
    data = r.json()
    assert data['name'] == raw_user['name']
    assert data['avatar'] == raw_user['avatar']


def test_detail_delete(session):
    populate_users(1)
    user_list_url = url_for('users.user_list')
    users = requests.get(user_list_url).json()['data']
    for user in users:
        user_detail_url = url_for('users.user_detail', username=user['username'])
        assert requests.delete(user_detail_url).status_code == 204
        assert requests.delete(user_detail_url).status_code == 404


def test_get_unexisting_user(session):
    user_detail_url = url_for('users.user_detail', username='unexisting_username')
    assert requests.get(user_detail_url).status_code == 404


def test_detail_get(session):
    raw_user = {
        'name': 'Carl Sagan',
        'avatar': 'carl-sagan'
    }
    user_list_url = url_for('users.user_list')
    r = requests.post(user_list_url, json=raw_user)
    username = r.json()['username']
    user_detail_url = url_for('users.user_detail', username=username)
    r = requests.get(user_detail_url)
    assert r.status_code == 200
    data = r.json() 
    assert data['name'] == raw_user['name']
    assert data['avatar'] == raw_user['avatar']


def test_get_users_list(session):
    populate_users(3)
    user_list_url = url_for('users.user_list')
    r = requests.get(user_list_url)
    assert r.status_code == 200
    data = r.json()['data']
    assert len(data) == 3
