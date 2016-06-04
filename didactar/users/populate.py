import json
import requests
from flask import url_for


def populate_users(ammount=None):
    url = url_for('users.user_list')
    data_file = open('didactar/users/data.json')
    items = json.load(data_file)
    for item in items[:ammount]:
        requests.post(url, json=item)
    return requests.get(url).json()['data']
