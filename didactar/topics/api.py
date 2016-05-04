import json
from flask import Blueprint
from flask import request

from .models import Topic
from .serializers import detail_serializer
from .serializers import list_serializer


topics = Blueprint('topics', __name__)


@topics.route('/topics', methods=['GET', 'POST'])
def topic_list():

    if request.method == 'GET':
        try:
            topics = Topic.all()
            return list_serializer(topics)
        except:
            return '', 400 
    
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))
            topic = Topic(data)
            topic.save()
            return detail_serializer(topic), 201
        except:
            return '', 400 


@topics.route('/topics/<topic_slug>', methods=['GET', 'DELETE'])
def topic_detail(topic_slug):

    if request.method == 'GET':
        try:
            topic = Topic.get_by_slug(topic_slug)
            if not topic:
                return '', 404
            return detail_serializer(topic)
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            topic = Topic.get_by_slug(topic_slug)
            if not topic:
                return '', 404
            topic.delete()
            return '', 204
        except:
            return '', 400
