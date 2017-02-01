import requests
from conftest import session, URL_PREFIX
from feynman.participations.utils.populate import prepopulate


def test_list_post(session):
    users, workshops, events = prepopulate()
    for event in events:
        for user in users:
            raw_participation = {'user': user, 'event': event}
            r = requests.post(URL_PREFIX + 'participations', json=raw_participation)
            assert r.status_code == 201
            participation = r.json()
            assert participation['user']['id'] == user['id']
            assert participation['event']['id'] == event['id']


def test_detail_delete(session):
    users, workshops, events = prepopulate()
    for user in users:
        for event in events:
            raw_participation = {'user': user, 'event': event}
            participation = requests.post(URL_PREFIX + 'participations', json=raw_participation).json()
            id = str(participation['id']) 
            assert requests.delete(URL_PREFIX + 'participations/' + id).status_code == 204
            assert requests.delete(URL_PREFIX + 'participations/' + id).status_code == 404


def test_get_unexisting_detail(session):
    r = requests.get(URL_PREFIX + 'participations/1234')
    assert r.status_code == 404


def test_detail_get(session):
    users, workshops, events = prepopulate()
    for event in events:
        for user in users:
            raw_participation = {'user': user, 'event': event}
            participation = requests.post(URL_PREFIX + 'participations', json=raw_participation).json()
            id = str(participation['id']) 
            r = requests.get(URL_PREFIX + 'participations/' + id)
            assert r.status_code == 200
            participation = r.json()
            assert participation['user']['id'] == user['id']
            assert participation['event']['id'] == event['id']


def test_get_event_participation_list(session):
    users, workshops, events = prepopulate()
    for event in events:
        for user in users:
            raw_participation = {'user': user, 'event': event}
            requests.post(URL_PREFIX + 'participations', json=raw_participation)
        r = requests.get(URL_PREFIX + 'events/' + event['slug'] + '/participations')
        assert r.status_code == 200
        participations = r.json()['data']
        assert len(participations) == 2


def test_user_participation_list(session):
    users, workshops, events = prepopulate()
    for user in users:
        for event in events:
            raw_participation = {'user': user, 'event': event}
            requests.post(URL_PREFIX + 'participations', json=raw_participation)
        r = requests.get(URL_PREFIX + 'users/' + user['username'] + '/participations')
        assert r.status_code == 200
        participations = r.json()['data']
        assert len(participations) == 2


def test_user_workshop_participation_list(session):
    users, workshops, events = prepopulate()
    for user in users:
        for event in events:
            raw_participation = {'user': user, 'event': event}
            requests.post(URL_PREFIX + 'participations', json=raw_participation)
        for workshop in workshops:
            r = requests.get(URL_PREFIX + 'users/' + user['username'] + '/participations?workshop=' + workshop['slug'])
            assert r.status_code == 200
            participations = r.json()['data']
            assert len(participations) == 2
