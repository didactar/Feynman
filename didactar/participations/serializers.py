from flask import jsonify


def serializer(participation):
    return {
        'id': participation.id,
        'event': {'id': participation.event_id},
        'user': {'id': participation.user_id}
    }

def participation_detail_serializer(participation):
    s = serializer(participation)
    return jsonify(s)

def participation_list_serializer(participations):
    data = [serializer(p) for p in participations]
    return jsonify(data=data)
