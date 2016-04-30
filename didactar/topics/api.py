import json
from flask import Blueprint
from flask import request
from .models import Topic
from .serializers import topic_detail_serializer
from .serializers import topic_list_serializer

from didactar.events.serializers import event_list_serializer
from didactar.events.models import Event


topics = Blueprint('topics', __name__)


@topics.route('/topics', methods=['GET', 'POST'])
def topic_list():

    if request.method == 'GET':
        topics = Topic.all()
        return topic_list_serializer(topics)
    
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        name = data['name']
        description = data['description']
        try:
            topic = Topic.new(name, description)
            return topic_detail_serializer(topic), 201
        except:
            return '', 400 



@topics.route('/topics/<slug>', methods=['GET', 'DELETE'])
def topic_detail(slug):

    if request.method == 'GET':
        topic = Topic.get(slug)
        if topic:
            return topic_detail_serializer(topic), 200
        else:
            return '', 404

    if request.method == 'DELETE':
        topic = Topic.get(slug)
        if topic:
            Topic.delete(slug)
            return '', 204
        else:
            return '', 404


@topics.route('/topics/<slug>/events', methods=['GET'])
def topic_event_list(slug):

    if request.method == 'GET':
        topic = Topic.get(slug)
        if topic:
            events = Event.filterByTopic(topic)
            return event_list_serializer(events), 200
        else:
            return '', 404
