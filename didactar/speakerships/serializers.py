from flask import jsonify

from didactar.events.models import Event
from didactar.users.models import User


def detail_dict(speakership):
    return {
        'id': speakership.id,
        'event': {'id': speakership.event_id},
        'user': {'id': speakership.user_id}
    }


def detail_dict_event(speakership):
    event_id = speakership.get_event_id()
    event = Event.get_by_id(event_id)
    return {
        'id': speakership.id,
        'event': {
            'slug': event.slug,
            'title': event.title,
            'description': event.description
        }
    }


def detail_dict_user(speakership):
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


def detail_serializer(speakership):
    d = detail_dict(speakership)
    return jsonify(d)


def list_serializer_user(speakerships):
    d = [detail_dict_user(p) for p in speakerships]
    return jsonify(data=d)


def list_serializer_event(speakerships):
    d = [detail_dict_event(p) for p in speakerships]
    return jsonify(data=d)
