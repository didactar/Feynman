from flask import jsonify


def serializer(marking):
    return {
        'id': marking.id,
        'event': {'id': marking.event_id},
        'topic': {'id': marking.topic_id}
    }

def marking_detail_serializer(marking):
    s = serializer(marking)
    return jsonify(s)

def marking_list_serializer(markings):
    data = [serializer(et) for et in markings]
    return jsonify(data=data)
