import json
from flask import Blueprint
from flask import request

from .models import EventTopic
from .serializers import event_topic_detail_serializer
from .serializers import event_topic_list_serializer

events_topics = Blueprint('events_topics', __name__)


@events_topics.route('/events/<event_slug>/topics', methods=['GET', 'POST'])
def event_topics_list(event_slug):

    if request.method == 'GET':
        event_topic_list = EventTopic.filter_by_event(event_slug)
        if not event_topic_list:
            return '', 400
        return event_topic_list_serializer(event_topic_list)
    
    if request.method == 'POST':
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        topic_slug = data['slug']
        event_topic = EventTopic.create(event_slug, topic_slug)
        if not event_topic:
            return '', 400
        return event_topic_detail_serializer(event_topic), 201


@events_topics.route('/topics/<topic_slug>/events', methods=['GET'])
def topic_events_list(topic_slug):

    if request.method == 'GET':
        event_topic_list = EventTopic.filter_by_topic(topic_slug)
        if not event_topic_list:
            return '', 400
        return event_topic_list_serializer(event_topic_list)


@events_topics.route('/events/<event_slug>/topics/<topic_slug>', methods=['GET', 'DELETE'])
def event_topic_detail(event_slug, topic_slug):

    if request.method == 'GET':
        event_topic = EventTopic.get(event_slug, topic_slug)
        if not event_topic:
            return '', 404
        return event_topic_detail_serializer(event_topic), 200

    if request.method == 'DELETE':
        event_topic = EventTopic.get(event_slug, topic_slug)
        if not event_topic:
            return '', 404
        event_topic.delete()
        return '', 204




