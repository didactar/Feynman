from flask import jsonify

from didactar.events.models import Event
from didactar.topics.models import Topic
from didactar.events.serializers import event_dict


def detail_dict(marking):
    return {
        'id': marking.id,
        'event': {'id': marking.event_id},
        'topic': {'id': marking.topic_id}
    }


def detail_dict_event(marking):
    event_id = marking.get_event_id()
    event = Event.get_by_id(event_id)
    return {
        'id': marking.id,
        'event': event_dict(event)
    }


def detail_dict_topic(marking):
    topic_id = marking.get_topic_id()
    topic = Topic.get_by_id(topic_id)
    return {
        'id': marking.id,
        'topic': {
            'name': topic.name,
            'description': topic.description,
            'slug': topic.slug,
            'image': topic.image
        }
    }


def detail_serializer(marking):
    d = detail_dict(marking)
    return jsonify(d)


def list_serializer_topic(markings):
    d = [detail_dict_topic(p) for p in markings]
    return jsonify(data=d)


def list_serializer_event(markings):
    d = [detail_dict_event(p) for p in markings]
    return jsonify(data=d)
