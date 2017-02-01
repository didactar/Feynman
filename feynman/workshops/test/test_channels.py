import requests
from flask import url_for
from conftest import session


def test_list_post(session):
    raw_workshop = {
        'name': 'Science and Stuff',
        'description': 'Description of the workshop Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    workshop_list_url = url_for('workshops.workshop_list')
    r = requests.post(workshop_list_url, json=raw_workshop)
    assert r.status_code == 201
    data = r.json()
    assert data['name'] == raw_workshop['name']
    assert data['description'] == raw_workshop['description']
    assert data['avatar'] == raw_workshop['avatar']
    assert data['image'] == raw_workshop['image']


def test_detail_delete(session):
    raw_workshop = {
        'name': 'Science and Stuff',
        'description': 'Description of the workshop Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    workshop_list_url = url_for('workshops.workshop_list')
    r = requests.post(workshop_list_url, json=raw_workshop)
    workshop_slug = r.json()['slug']
    workshop_detail_url = url_for('workshops.workshop_detail', workshop_slug=workshop_slug)
    assert requests.delete(workshop_detail_url).status_code == 204
    assert requests.delete(workshop_detail_url).status_code == 404


def test_get_unexisting_workshop(session):
    workshop_detail_url = url_for('workshops.workshop_detail', workshop_slug='unexisting_slug')
    assert requests.get(workshop_detail_url).status_code == 404


def test_detail_get(session):
    raw_workshop = {
        'name': 'Science and Stuff',
        'description': 'Description of the workshop Science and Stuff',
        'avatar': 'science-avatar',
        'image': 'science-image'
    }
    workshop_list_url = url_for('workshops.workshop_list')
    r = requests.post(workshop_list_url, json=raw_workshop)
    workshop_slug = r.json()['slug']
    workshop_detail_url = url_for('workshops.workshop_detail', workshop_slug=workshop_slug)
    r = requests.get(workshop_detail_url)
    assert r.status_code == 200
    data = r.json() 
    assert data['name'] == raw_workshop['name']
    assert data['description'] == raw_workshop['description']
    assert data['avatar'] == raw_workshop['avatar']
    assert data['image'] == raw_workshop['image']


def test_get_workshops_list(session):
    raw_workshops = [
        {
            'name': 'Science and Stuff',
            'description': 'Description of the workshop Science and Stuff',
            'avatar': 'science',
            'image': 'science'
        },
        {
            'name': 'Programming for beginners',
            'description': 'Description of the workshop Programming for begginers',
            'avatar': 'programming',
            'image': 'programming'
        },
        {
            'name': 'General Culture',
            'description': 'Description of the workshop General Culture',
            'avatar': 'culture',
            'image': 'culture'
        }
    ]
    workshop_list_url = url_for('workshops.workshop_list')
    for raw_workshop in raw_workshops:
        requests.post(workshop_list_url, json=raw_workshop)
    r = requests.get(workshop_list_url)
    assert r.status_code == 200
    workshops = r.json()['data']
    assert len(workshops) == 3
    for raw_workshop, workshop in zip(raw_workshops, workshops):
        assert workshop['name'] == raw_workshop['name']
        assert workshop['description'] == raw_workshop['description']
        assert workshop['avatar'] == raw_workshop['avatar']
        assert workshop['image'] == raw_workshop['image']
