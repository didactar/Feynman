import pytest
import requests
from slugify import slugify
import json

from didactar import BASE_URL
from didactar import setup_test_app

URL = BASE_URL + 'channels'

@pytest.fixture(scope='module')
def setup_channels():
    setup_test_app()


def test_create_get_delete_channels(setup_channels):

    with open('didactar/channels/test_channels_data.json') as f:
        CHANNELS = json.load(f)

    # create channels
    for channel in CHANNELS:
        r = requests.post(URL, json=channel) 
        assert r.status_code == 201

    # get channels list
    r = requests.get(URL) 
    assert r.status_code == 200

    # check channels list length
    r_content = r.content.decode('utf-8')
    data = json.loads(r_content)
    assert len(data['data']) == len(CHANNELS)

    # get channel details
    for channel in CHANNELS:

        # check it exists
        slug = slugify(channel['name'], to_lower=True)
        url = URL + '/' + slug
        r = requests.get(url) 
        assert r.status_code == 200

        # check correct data
        data = json.loads(r.content.decode('utf-8'))
        assert data['slug'] == slug
        assert data['description'] == channel['description']

        # delete channel
        assert requests.delete(url).status_code == 204
        assert requests.delete(url).status_code == 404
        

def test_get_unexisting_channel():
    unexisting_channel_slugs = ['aaa','bbb','ccc']
    for slug in unexisting_channel_slugs:
        r = requests.get(URL + '/' + slug)
        assert r.status_code == 404
