import json
import requests
from flask import url_for


with open('feynman/workshops/utils/loremipsum.md') as f:
    guide = f.read()


def populate_workshops(ammount=None):
    url = url_for('workshops.workshop_list')
    data_file = open('feynman/workshops/utils/data.json')
    workshops = json.load(data_file)
    for workshop in workshops[:ammount]:
        workshop['guide'] = guide
        requests.post(url, json=workshop)
    return requests.get(url).json()['data']
