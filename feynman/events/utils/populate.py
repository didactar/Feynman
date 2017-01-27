import json
import requests
from flask import url_for


def populate_events(channel, ammount=None):
    event_list_url = url_for('events.event_list')
    data_file = open('feynman/events/utils/data.json')
    events = json.load(data_file)
    for event in events[:ammount]:
        event['channel'] = channel
        requests.post(event_list_url, json=event)
    channel_event_list_url = url_for('events.channel_event_list', channel_slug=channel['slug'])
    return requests.get(channel_event_list_url).json()['data']
