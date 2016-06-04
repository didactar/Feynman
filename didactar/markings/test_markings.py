import requests
from flask import url_for
from fixtures import session, app

from didactar.channels.populate import populate_channels
from didactar.events.populate import populate_events
from didactar.topics.populate import populate_topics


def test_list_post(session):
    for topic in populate_topics(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('markings.marking_list')
                raw_marking = {'topic': topic, 'event': event}
                r = requests.post(list_url, json=raw_marking)
                assert r.status_code == 201
                marking = r.json()
                assert marking['topic']['id'] == topic['id']
                assert marking['event']['id'] == event['id']


def test_detail_delete(session):
    for topic in populate_topics(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('markings.marking_list')
                raw_marking = {'topic': topic, 'event': event}
                marking = requests.post(list_url, json=raw_marking).json()
                detail_url = url_for('markings.marking_detail', id=marking['id'])
                assert requests.delete(detail_url).status_code == 204
                assert requests.delete(detail_url).status_code == 404


def test_get_unexisting_detail(session):
    detail_url = url_for('markings.marking_detail', id='999')
    assert requests.get(detail_url).status_code == 404


def test_detail_get(session):
    for topic in populate_topics(1):
        for channel in populate_channels(1):
            for event in populate_events(channel, 1):
                list_url = url_for('markings.marking_list')
                raw_marking = {'topic': topic, 'event': event}
                marking = requests.post(list_url, json=raw_marking).json()
                detail_url = url_for('markings.marking_detail', id=marking['id'])
                r = requests.get(detail_url)
                assert r.status_code == 200
                marking = r.json()
                assert marking['topic']['id'] == topic['id']
                assert marking['event']['id'] == event['id']


def test_get_event_marking_list(session):
    topics = populate_topics(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for topic in topics:
                list_url = url_for('markings.marking_list')
                raw_marking = {'topic': topic, 'event': event}
                requests.post(list_url, json=raw_marking)
        for event in events:
            event_marking_list_url = url_for('markings.event_marking_list', event_slug=event['slug'])
            r = requests.get(event_marking_list_url)
            assert r.status_code == 200
            markings = r.json()['data']
            assert len(markings) == 2


def test_topic_marking_list(session):
    topics = populate_topics(2)
    for channel in populate_channels(2):
        events = populate_events(channel, 2)
        for event in events:
            for topic in topics:
                list_url = url_for('markings.marking_list')
                raw_marking = {'topic': topic, 'event': event}
                requests.post(list_url, json=raw_marking)
    for topic in topics:
        topic_marking_list_url = url_for('markings.topic_marking_list', topic_slug=topic['slug'])
        r = requests.get(topic_marking_list_url)
        assert r.status_code == 200
        markings = r.json()['data']
        assert len(markings) == 4
