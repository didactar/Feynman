import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../')

import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app


def populate_database():


    with open('didactar/channels/test_channels_data.json') as f:
        for channel in json.load(f):
            requests.post(BASE_URL + 'channels', json=channel) 

    with open('didactar/events/test_events_data.json') as f:
        for event in json.load(f):
            requests.post(BASE_URL + 'events', json=event) 

    with open('didactar/users/test_users_data.json') as f:
        for user in json.load(f):
            requests.post(BASE_URL + 'users', json=user) 


@pytest.fixture(scope='module')
def setup_speakerships():
    setup_test_app()
    populate_database()


def test_create_get_delete_speakerships(setup_speakerships):

    # get existing events and users
    
    events_request = requests.get(BASE_URL + 'events')
    events_content = events_request.content.decode('utf-8')
    events = json.loads(events_content)['data']
    assert len(events)

    users_request = requests.get(BASE_URL + 'users')
    users_content = users_request.content.decode('utf-8')
    users = json.loads(users_content)['data']
    assert len(users)

    # create each speaker for each event
    for event in events:
        for user in users:
            list_url = BASE_URL + 'speakerships'
            data = {'event': event, 'user': user}
            r = requests.post(list_url, json=data)
            assert r.status_code == 201

    # check all speakers for each event    
    for event in events:
        user_list_url = BASE_URL + 'events/' + event['slug'] + '/speakerships'
        r = requests.get(user_list_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        event_users = json.loads(request_content)['data']
        assert len(event_users) == len(users)    

    # check all events for each user    
    for user in users:
        event_list_url = BASE_URL + 'users/' + user['username'] + '/speakerships'
        r = requests.get(event_list_url)
        assert r.status_code == 200
        request_content = r.content.decode('utf-8')
        user_events = json.loads(request_content)['data']
        assert len(user_events) == len(events)    

    # delete all speakerships
    for user in users:
        user_speakerships = BASE_URL + 'users/' + user['username'] + '/speakerships'
        r = requests.get(user_speakerships)
        request_content = r.content.decode('utf-8')
        speakerships = json.loads(request_content)['data']
        for p in speakerships:
            speakership_detail_url = '{}speakerships/{}'.format(BASE_URL, p['id'])
            assert requests.delete(speakership_detail_url).status_code == 204
            assert requests.delete(speakership_detail_url).status_code == 404
