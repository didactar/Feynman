import json
import requests
from flask import url_for


def populate_markings(event, topics, ammount=None):
    url = url_for('markings.marking_list')
    for topic in topics[:ammount]:
        raw_marking = {'topic': topic, 'event': event}
        r = requests.post(url, json=raw_marking)
    event_marking_list_url = url_for('markings.event_marking_list', event_slug=event['slug'])
    return requests.get(event_marking_list_url).json()['data']

