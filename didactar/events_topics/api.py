import json
from flask import Blueprint
from flask import request

from .models import EventTopic

events_topics = Blueprint('events_topics', __name__)


@events_topics.route('/<event_slug>/topics', methods=['GET', 'POST'])
def event_topic_list():

    if request.method == 'GET':
        event_topic_list = EventTopic.filter_by_event(event_slug)
        return event_topic_list_serializer(event_topic_list)
    
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        topic_slug = data['topic']['slug']
        event_topic = EventTopic.create(event_slug=event_slug, topic_slug=topic_slug)
        return event_topic_detail_serializer(event_topic), 201



@events_topics.route('/<event_slug>/topics/<topic_slug>', methods=['GET', 'DELETE'])
def event_topic_detail(slug):

    if request.method == 'GET':
        event_topic = EventTopic.get(event_slug=event_slug, topic_slug=topic_slug)
        if not event_topic:
            return '', 404
        return event_topic_detail_serializer(event), 200

    if request.method == 'DELETE':
        event_topic = EventTopic.get(event_slug=event_slug, topic_slug=topic_slug)
        if not event_topic:
            return '', 404
        event_topic.delete()
        return '', 204
