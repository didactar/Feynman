import json
import os
import requests
import random
from didactar import BASE_URL


def select_max(complete_list, max_amount):
    sample_size = random.randrange(max_amount)
    for i in random.sample(complete_list, sample_size):
        yield i


def get_list(url):
    full_url = BASE_URL + url
    request = requests.get(full_url)
    content = request.content.decode('utf-8')
    return json.loads(content)['data']


def populate_generic_resource(resource_name):
    print('Populating ' + resource_name + '...')
    filename = './data/' + resource_name + '.json'
    input_file = os.path.join(os.path.dirname(__file__), filename)
    with open(input_file) as f:    
        for item in json.load(f):
            r = requests.post(BASE_URL + resource_name, json=item) 
            if r.status_code != 201:
                print('Error creating ' + str(item))
                exit()


def populate_events():
    print('Populating events...')
    url = BASE_URL + 'events'
    filename = './data/events.json'
    input_file = os.path.join(os.path.dirname(__file__), filename)
    channels = get_list('channels')
    with open(input_file) as f:    
        for event in json.load(f):
            for channel in channels:
                event['channel'] = channel
                r = requests.post(url, json=event) 
                if r.status_code != 201:
                    print('Error creating ' + str(item))
                    exit()


def populate_relationship(relationship, resource_1, resource_2, max_amount):
    print('Populating ' + relationship + '...')
    r1_list = get_list(resource_1[1])
    r2_list = get_list(resource_2[1])
    for r1 in r1_list: 
        for r2 in select_max(r2_list, max_amount):
            data = {resource_1[0]: r1, resource_2[0]: r2}
            r = requests.post(BASE_URL + relationship, json=data)
            if r.status_code != 201:
                print('\nError creating ' + str(data))
                exit()


def populate_database():
    populate_generic_resource('topics')
    populate_generic_resource('channels')
    populate_generic_resource('users')
    populate_events()
    populate_relationship('markings', ['event', 'events'], ['topic','topics'], 3)
    populate_relationship('participations', ['event', 'events'], ['user', 'users'], 10)
    populate_relationship('speakerships', ['event', 'events'], ['user', 'users'], 3)
