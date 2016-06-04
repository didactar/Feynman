import json
import requests
from flask import url_for


def populate_topics(ammount=None):
    url = url_for('topics.topic_list')
    data_file = open('didactar/topics/data.json')
    topics = json.load(data_file)
    for topic in topics[:ammount]:
        requests.post(url, json=topic)
    return requests.get(url).json()['data']
