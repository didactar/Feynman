from flask import jsonify

from didactar.participations.models import Participation

def serializer(event):
    p_count = Participation.event_participations_count(event)
    return {
        'id': event.id, 
        'title': event.title, 
        'slug': event.slug,
        'description': event.description,
        'participationsCount': p_count
    }


def event_detail_serializer(event):
    s = serializer(event)
    return jsonify(s)


def event_list_serializer(events):
    data = [serializer(event) for event in events]
    return jsonify(data=data)
