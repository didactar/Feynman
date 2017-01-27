import requests
from flask import url_for
from conftest import session


def test_list_post(session):
    raw_channel = {
        'name': 'Science and Stuff',
        'description': 'Description of the channel Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    channel_list_url = url_for('channels.channel_list')
    r = requests.post(channel_list_url, json=raw_channel)
    assert r.status_code == 201
    data = r.json()
    assert data['name'] == raw_channel['name']
    assert data['description'] == raw_channel['description']
    assert data['avatar'] == raw_channel['avatar']
    assert data['image'] == raw_channel['image']


def test_detail_delete(session):
    raw_channel = {
        'name': 'Science and Stuff',
        'description': 'Description of the channel Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    channel_list_url = url_for('channels.channel_list')
    r = requests.post(channel_list_url, json=raw_channel)
    channel_slug = r.json()['slug']
    channel_detail_url = url_for('channels.channel_detail', channel_slug=channel_slug)
    assert requests.delete(channel_detail_url).status_code == 204
    assert requests.delete(channel_detail_url).status_code == 404


def test_get_unexisting_channel(session):
    channel_detail_url = url_for('channels.channel_detail', channel_slug='unexisting_slug')
    assert requests.get(channel_detail_url).status_code == 404


def test_detail_get(session):
    raw_channel = {
        'name': 'Science and Stuff',
        'description': 'Description of the channel Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    channel_list_url = url_for('channels.channel_list')
    r = requests.post(channel_list_url, json=raw_channel)
    channel_slug = r.json()['slug']
    channel_detail_url = url_for('channels.channel_detail', channel_slug=channel_slug)
    r = requests.get(channel_detail_url)
    assert r.status_code == 200
    data = r.json() 
    assert data['name'] == raw_channel['name']
    assert data['description'] == raw_channel['description']
    assert data['avatar'] == raw_channel['avatar']
    assert data['image'] == raw_channel['image']


def test_get_channels_list(session):
    raw_channels = [
        {
            'name': 'Science and Stuff',
            'description': 'Description of the channel Science and Stuff',
            'avatar': 'science',
            'image': 'science'
        },
        {
            'name': 'Programming for beginners',
            'description': 'Description of the channel Programming for begginers',
            'avatar': 'programming',
            'image': 'programming'
        },
        {
            'name': 'General Culture',
            'description': 'Description of the channel General Culture',
            'avatar': 'culture',
            'image': 'culture'
        }
    ]
    channel_list_url = url_for('channels.channel_list')
    for raw_channel in raw_channels:
        requests.post(channel_list_url, json=raw_channel)
    r = requests.get(channel_list_url)
    assert r.status_code == 200
    channels = r.json()['data']
    assert len(channels) == 3
    for raw_channel, channel in zip(raw_channels, channels):
        assert channel['name'] == raw_channel['name']
        assert channel['description'] == raw_channel['description']
        assert channel['avatar'] == raw_channel['avatar']
        assert channel['image'] == raw_channel['image']
