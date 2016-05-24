from flask import jsonify

from didactar.participations.models import Participation
from didactar.channels.models import Channel



def channel_dict(channel_id):
    channel = Channel.get_by_id(channel_id) 
    return {
        'id': channel.id,
        'slug': channel.slug,
        'name': channel.name,
        'avatar': channel.avatar
    }


def event_dict(event):
    return {
        'id': event.id, 
        'title': event.title, 
        'slug': event.slug,
        'channel': channel_dict(event.channel_id),
        'description': event.description,
        'participationCount': Participation.event_participation_count(event)
    }


def detail_serializer(event):
    s = event_dict(event)
    return jsonify(s)


def list_serializer(events):
    data = [event_dict(event) for event in events]
    return jsonify(data=data)
