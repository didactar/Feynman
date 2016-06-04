import json
import requests
from flask import url_for


def populate_hostings(event, users, ammount=None):
    url = url_for('hostings.hosting_list')
    for user in users[:ammount]:
        raw_hosting = {'user': user, 'event': event}
        r = requests.post(url, json=raw_hosting)
    event_hosting_list_url = url_for(
        'hostings.event_hosting_list', 
        event_slug=event['slug'])
    return requests.get(event_hosting_list_url).json()['data']
