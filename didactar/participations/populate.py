import json
import requests
from flask import url_for


def populate_participations(event, users, ammount=None):
    url = url_for('participations.participation_list')
    for user in users[:ammount]:
        raw_participation = {'user': user, 'event': event}
        r = requests.post(url, json=raw_participation)
    event_participation_list_url = url_for(
        'participations.event_participation_list', 
        event_slug=event['slug'])
    return requests.get(event_participation_list_url).json()['data']
