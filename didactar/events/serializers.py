from flask import jsonify

from didactar.users.models import User
from didactar.speakerships.models import Speakership
from didactar.participations.models import Participation
from didactar.channels.models import Channel


def speaker_dict(speakership):
    user_id = speakership.get_user_id()
    user = User.get_by_id(user_id)
    return {
        'id': speakership.id,
        'user': {
            'username': user.username,
            'name': user.name,
            'about': user.about,
            'avatar': user.avatar
        }
    }


def speakers_dict(event):
    speakerships = Speakership.filter_by_event(event)
    return [speaker_dict(s) for s in speakerships]


def channel_dict(event):
    channel = Channel.get_by_id(event.channel_id) 
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
        'channel': channel_dict(event),
        'description': event.description,
        'participationCount': Participation.event_participation_count(event),
        'speakers': speakers_dict(event)
    }


def detail_serializer(event):
    s = event_dict(event)
    return jsonify(s)


def list_serializer(events):
    data = [event_dict(event) for event in events]
    return jsonify(data=data)
