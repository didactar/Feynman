import requests
from flask import url_for
from conftest import session
from feynman.channels.utils.populate import populate_channels


def test_list_post(session):
    raw_event = {
        'title': 'Donec consequat massa non accumsan eleifend.',
        'description': 'In consectetur lacus at massa rhoncus aliquet. Nulla non turpis fermentum, porttitor mi ac, facilisis risus. Aenean tincidunt imperdiet ante, at dictum lectus imperdiet quis. In tristique auctor posuere. Mauris pellentesque ex purus, nec gravida turpis consectetur et. Nulla facilisi. Phasellus luctus dapibus lectus, sed lobortis felis dapibus ac. Integer augue nibh, hendrerit quis vehicula in, condimentum et nulla. Nam porta pulvinar nunc, in auctor nisl rhoncus eget. Praesent vitae justo sed orci consectetur pellentesque. Phasellus rhoncus dolor nec orci luctus ullamcorper. Pellentesque consectetur lobortis tellus, sed tincidunt justo sollicitudin a.'
    }
    for channel in populate_channels(1):
        event_list_url = url_for('events.event_list')
        raw_event['channel'] = channel
        r = requests.post(event_list_url, json=raw_event)
        assert r.status_code == 201
        data = r.json()
        assert data['title'] == raw_event['title']
        assert data['channel']['id'] == raw_event['channel']['id']
        assert data['description'] == raw_event['description']


def test_detail_delete(session):
    raw_event = {
        'title': 'Donec consequat massa non accumsan eleifend.',
        'description': 'In consectetur lacus at massa rhoncus aliquet. Nulla non turpis fermentum, porttitor mi ac, facilisis risus. Aenean tincidunt imperdiet ante, at dictum lectus imperdiet quis. In tristique auctor posuere. Mauris pellentesque ex purus, nec gravida turpis consectetur et. Nulla facilisi. Phasellus luctus dapibus lectus, sed lobortis felis dapibus ac. Integer augue nibh, hendrerit quis vehicula in, condimentum et nulla. Nam porta pulvinar nunc, in auctor nisl rhoncus eget. Praesent vitae justo sed orci consectetur pellentesque. Phasellus rhoncus dolor nec orci luctus ullamcorper. Pellentesque consectetur lobortis tellus, sed tincidunt justo sollicitudin a.'
    }
    for channel in populate_channels(1):
        event_list_url = url_for('events.event_list')
        raw_event['channel'] = channel
        event = requests.post(event_list_url, json=raw_event).json()
        event_url = url_for('events.event_detail', event_slug=event['slug'])
        assert requests.delete(event_url).status_code == 204
        assert requests.delete(event_url).status_code == 404


def test_get_unexisting_event_from_existing_channel(session):
    url = url_for('events.event_detail', event_slug='unexisting_slug')
    assert requests.get(url).status_code == 404


def test_detail_get(session):
    for channel in populate_channels(1):
        raw_event = {
            'title': 'Donec consequat massa non accumsan eleifend.',
            'description': 'In consectetur lacus at massa rhoncus aliquet. Nulla non turpis fermentum, porttitor mi ac, facilisis risus. Aenean tincidunt imperdiet ante, at dictum lectus imperdiet quis. In tristique auctor posuere. Mauris pellentesque ex purus, nec gravida turpis consectetur et. Nulla facilisi. Phasellus luctus dapibus lectus, sed lobortis felis dapibus ac. Integer augue nibh, hendrerit quis vehicula in, condimentum et nulla. Nam porta pulvinar nunc, in auctor nisl rhoncus eget. Praesent vitae justo sed orci consectetur pellentesque. Phasellus rhoncus dolor nec orci luctus ullamcorper. Pellentesque consectetur lobortis tellus, sed tincidunt justo sollicitudin a.',
            'channel': channel
        }
        event_list_url = url_for('events.event_list')
        raw_event['channel'] = channel
        event = requests.post(event_list_url, json=raw_event).json()
        event_url = url_for('events.event_detail', channel_slug=channel['slug'], event_slug=event['slug'])
        r = requests.get(event_url)
        assert r.status_code == 200
        data = r.json()
        assert data['title'] == raw_event['title']
        assert data['description'] == raw_event['description']
        assert data['channel']['id'] == raw_event['channel']['id']


def test_get_channel_event_list(session):
    raw_events = [
        {
            'title': 'Donec consequat massa non accumsan eleifend.',
            'description': 'In consectetur lacus at massa rhoncus aliquet. Nulla non turpis fermentum, porttitor mi ac, facilisis risus. Aenean tincidunt imperdiet ante, at dictum lectus imperdiet quis. In tristique auctor posuere. Mauris pellentesque ex purus, nec gravida turpis consectetur et. Nulla facilisi. Phasellus luctus dapibus lectus, sed lobortis felis dapibus ac. Integer augue nibh, hendrerit quis vehicula in, condimentum et nulla. Nam porta pulvinar nunc, in auctor nisl rhoncus eget. Praesent vitae justo sed orci consectetur pellentesque. Phasellus rhoncus dolor nec orci luctus ullamcorper. Pellentesque consectetur lobortis tellus, sed tincidunt justo sollicitudin a.'
        },
        {
            'title': 'Phasellus molestie enim vitae urna volutpat, sed volutpat tortor condimentum.',
            'description': 'Suspendisse ut tellus sit amet ex iaculis facilisis. Nam non aliquam lectus. Vestibulum ac mi ante. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In congue elit libero, euismod gravida diam aliquam vitae. Etiam sagittis sapien vitae odio elementum, a pretium lorem sodales. Fusce eget lacinia nisi'
        },
        {
            'title': 'Praesent aliquam dui ac odio accumsan, vel sodales urna sollicitudin.',
            'description': 'Suspendisse tempus imperdiet purus, sit amet porttitor orci. Vestibulum nec lobortis odio. Donec nec mollis lorem. Sed ullamcorper purus in placerat imperdiet. In placerat quam sit amet nisl placerat, at aliquam ligula mattis. Pellentesque id egestas magna, at auctor diam. Phasellus venenatis nisl id turpis ultricies, at venenatis orci bibendum. In hendrerit pulvinar sodales. Maecenas suscipit lectus elit, quis egestas augue tempor et. Morbi imperdiet vestibulum lacus id eleifend. Nam suscipit tincidunt tellus, vitae porttitor nisl ornare vitae. Maecenas elementum quam id tortor pretium, ut euismod libero suscipit. Suspendisse suscipit sit amet ligula at blandit. Praesent et ultrices est. Integer faucibus dapibus tortor quis dignissim.'
        }
    ]
    event_list_url = url_for('events.event_list')
    channels = populate_channels(1)
    for channel in channels:
        for raw_event in raw_events:
            raw_event['channel'] = channel
            requests.post(event_list_url, json=raw_event)
    for channel in channels:
        channel_event_list_url = url_for('events.channel_event_list', channel_slug=channel['slug'])
        r = requests.get(channel_event_list_url)
        assert r.status_code == 200
        events = r.json()['data']
        assert len(events) == 3
