import json
import requests
from flask import url_for


def populate_channels(ammount=None):
    url = url_for('channels.channel_list')
    data_file = open('feynman/channels/utils/data.json')
    channels = json.load(data_file)
    for channel in channels[:ammount]:
        requests.post(url, json=channel)
    return requests.get(url).json()['data']
