import json
from flask import Blueprint
from flask import request
from .models import Topic
from .serializers import topic_detail_serializer
from .serializers import topic_list_serializer


topics = Blueprint('topics', __name__)


@topics.route('/api/v1/topics', methods=['GET', 'POST'])
def topic_list():

    if request.method == 'GET':
        topics = Topic.all()
        return topic_list_serializer(topics)
    
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        name = data['name']
        description = data['description']
        topic = Topic.new(name, description)
        return topic_detail_serializer(topic), 201



@topics.route('/api/v1/topics/<slug>', methods=['GET', 'DELETE'])
def topic_detail(slug):

    if request.method == 'GET':
        topic = Topic.get(slug)
        if topic:
            return topic_detail_serializer(topic), 200
        else:
            return '', 404

    if request.method == 'DELETE':
        Topic.delete(slug)
        return '', 204
