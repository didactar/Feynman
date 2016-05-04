from flask import jsonify

from didactar.participations.models import Participation

def event_dict(event):
    p_count = Participation.event_participation_count(event)
    return {
        'id': event.id, 
        'title': event.title, 
        'slug': event.slug,
        'description': event.description,
        'participationCount': p_count
    }


def detail_serializer(event):
    s = event_dict(event)
    return jsonify(s)


def list_serializer(events):
    data = [event_dict(event) for event in events]
    return jsonify(data=data)
