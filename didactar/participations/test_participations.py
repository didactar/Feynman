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
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                r = requests.post(list_url, json=raw_participation)
                assert r.status_code == 201
                participation = r.json()
                assert participation['user']['id'] == user['id']
                assert participation['event']['id'] == event['id']


def test_detail_delete(session):
    for user in populate_users(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                participation = requests.post(list_url, json=raw_participation).json()
                detail_url = url_for('participations.participation_detail', id=participation['id'])
                assert requests.delete(detail_url).status_code == 204
                assert requests.delete(detail_url).status_code == 404


def test_get_unexisting_detail(session):
    detail_url = url_for('participations.participation_detail', id='999')
    assert requests.get(detail_url).status_code == 404


def test_detail_get(session):
    for user in populate_users(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                participation = requests.post(list_url, json=raw_participation).json()
                detail_url = url_for('participations.participation_detail', id=participation['id'])
                r = requests.get(detail_url)
                assert r.status_code == 200
                participation = r.json()
                assert participation['user']['id'] == user['id']
                assert participation['event']['id'] == event['id']


def test_get_event_participation_list(session):
    users = populate_users(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                requests.post(list_url, json=raw_participation)
        for event in events:
            event_participation_list_url = url_for('participations.event_participation_list', event_slug=event['slug'])
            r = requests.get(event_participation_list_url)
            assert r.status_code == 200
            participations = r.json()['data']
            assert len(participations) == 2

def test_user_participation_list(session):
    users = populate_users(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                requests.post(list_url, json=raw_participation)
    for user in users:
        user_participation_list_url = url_for('participations.user_participation_list', username=user['username'])
        r = requests.get(user_participation_list_url)
        assert r.status_code == 200
        participations = r.json()['data']
        assert len(participations) == 4


def test_user_channel_participation_list(session):
    users = populate_users(2)
    channels = populate_channels(2)
    for channel in channels:
        events = populate_events(channel, 2)
        for event in events:
            for user in users:
                list_url = url_for('participations.participation_list')
                raw_participation = {'user': user, 'event': event}
                requests.post(list_url, json=raw_participation)
    for channel in channels:
        for user in users:
            url = url_for('participations.user_participation_list', username=user['username'], channel=channel['slug'])
            r = requests.get(url)
            assert r.status_code == 200
            participations = r.json()['data']
            assert len(participations) == 2
            for p in participations:
                assert p['event']['channel']['slug'] == channel['slug']
