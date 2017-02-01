import json
import requests
from flask import url_for


def populate_workshops(ammount=None):
    url = url_for('workshops.workshop_list')
    data_file = open('feynman/workshops/utils/data.json')
    workshops = json.load(data_file)
    for workshop in workshops[:ammount]:
        requests.post(url, json=workshop)
    return requests.get(url).json()['data']
