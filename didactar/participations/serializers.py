from flask import jsonify

from didactar.events.models import Event
from didactar.users.models import User


def detail_dict(participation):
    return {
        'id': participation.id,
        'event': {'id': participation.event_id},
        'user': {'id': participation.user_id}
    }


def detail_dict_event(participation):
    event_id = participation.get_event_id()
    event = Event.get_by_id(event_id)
    return {
        'id': participation.id,
        'event': {
            'slug': event.slug,
            'title': event.title,
            'description': event.description
        }
    }


def detail_dict_user(participation):
    user_id = participation.get_user_id()
    user = User.get_by_id(user_id)
    return {
        'id': participation.id,
        'user': {
            'username': user.username,
            'name': user.name,
            'about': user.about,
            'avatar': user.avatar
        }
    }


def detail_serializer(participation):
    d = detail_dict(participation)
    return jsonify(d)


def list_serializer_user(participations):
    d = [detail_dict_user(p) for p in participations]
    return jsonify(data=d)


def list_serializer_event(participations):
    d = [detail_dict_event(p) for p in participations]
    return jsonify(data=d)
