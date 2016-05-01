from flask import jsonify


def serializer(event_topic):
    return {
        'id': event_topic.id,
        'event': {'id': event_topic.event_id},
        'topic': {'id': event_topic.topic_id}
    }

def event_topic_detail_serializer(event_topic):
    s = serializer(event_topic)
    return jsonify(s)

def event_topic_list_serializer(events_topics):
    data = [serializer(et) for et in events_topics]
    return jsonify(data=data)
