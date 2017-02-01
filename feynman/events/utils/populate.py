import json
import requests
from flask import url_for


def populate_events(workshop, ammount=None):
    event_list_url = url_for('events.event_list')
    data_file = open('feynman/events/utils/data.json')
    events = json.load(data_file)
    for event in events[:ammount]:
        event['workshop'] = workshop
        requests.post(event_list_url, json=event)
    workshop_event_list_url = url_for('events.workshop_event_list', workshop_slug=workshop['slug'])
    return requests.get(workshop_event_list_url).json()['data']
