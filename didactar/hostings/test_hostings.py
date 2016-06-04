import requests
from flask import url_for
from fixtures import session, app

from didactar.users.populate import populate_users
from didactar.events.populate import populate_events
from didactar.channels.populate import populate_channels


def test_list_post(session):
    for user in populate_users(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                r = requests.post(list_url, json=raw_hosting)
                assert r.status_code == 201
                hosting = r.json()
                assert hosting['user']['id'] == user['id']
                assert hosting['event']['id'] == event['id']


def test_detail_delete(session):
    for user in populate_users(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                hosting = requests.post(list_url, json=raw_hosting).json()
                detail_url = url_for('hostings.hosting_detail', id=hosting['id'])
                assert requests.delete(detail_url).status_code == 204
                assert requests.delete(detail_url).status_code == 404


def test_get_unexisting_detail(session):
    detail_url = url_for('hostings.hosting_detail', id='999')
    assert requests.get(detail_url).status_code == 404


def test_detail_get(session):
    for user in populate_users(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                hosting = requests.post(list_url, json=raw_hosting).json()
                detail_url = url_for('hostings.hosting_detail', id=hosting['id'])
                r = requests.get(detail_url)
                assert r.status_code == 200
                hosting = r.json()
                assert hosting['user']['id'] == user['id']
                assert hosting['event']['id'] == event['id']


def test_get_event_hosting_list(session):
    users = populate_users(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                requests.post(list_url, json=raw_hosting)
        for event in events:
            event_hosting_list_url = url_for('hostings.event_hosting_list', event_slug=event['slug'])
            r = requests.get(event_hosting_list_url)
            assert r.status_code == 200
            hostings = r.json()['data']
            assert len(hostings) == 2

def test_user_hosting_list(session):
    users = populate_users(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                requests.post(list_url, json=raw_hosting)
    for user in users:
        user_hosting_list_url = url_for('hostings.user_hosting_list', username=user['username'])
        r = requests.get(user_hosting_list_url)
        assert r.status_code == 200
        hostings = r.json()['data']
        assert len(hostings) == 4


def test_user_channel_hosting_list(session):
    users = populate_users(2)
    channels = populate_channels(2)
    for channel in channels:
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('hostings.hosting_list')
                raw_hosting = {'user': user, 'event': event}
                requests.post(list_url, json=raw_hosting)
    for channel in channels:
        for user in users:
            url = url_for('hostings.user_hosting_list', username=user['username'], channel=channel['slug'])
            r = requests.get(url)
            assert r.status_code == 200
            hostings = r.json()['data']
            assert len(hostings) == 2
            for p in hostings:
                assert p['event']['channel']['slug'] == channel['slug']
