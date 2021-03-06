import requests
from flask import url_for
from conftest import URL_PREFIX
from feynman.users.utils.populate import populate_users
from feynman.events.utils.populate import populate_events
from feynman.workshops.utils.populate import populate_workshops


def prepopulate():
    users = populate_users(2)
    workshops = populate_workshops(1)
    for workshop in workshops:
        populate_events(workshop, 2)
    events = requests.get(URL_PREFIX + 'events').json()['data']
    return users, workshops, events


def populate_participations(event, users, ammount=None):
    url = url_for('participations.participation_list')
    for user in users[:ammount]:
        raw_participation = {'user': user, 'event': event}
        r = requests.post(url, json=raw_participation)
    event_participation_list_url = url_for(
        'participations.event_participation_list', 
        event_slug=event['slug'])
    return requests.get(event_participation_list_url).json()['data']
