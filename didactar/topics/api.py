from flask import Blueprint
from flask import request
from flask import jsonify
from flask import url_for

from .models import Topic

from .serializers import topic_detail_serializer
from .serializers import topic_list_serializer


topics = Blueprint('topics', __name__)


@topics.route('/topics', methods=['GET', 'POST'])
def topic_list():

    if request.method == 'GET':
        topics = Topic.get_all()
        response = topic_list_serializer(topics)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        topic = Topic(data)
        topic.save()
        response = topic_detail_serializer(topic)
        return jsonify(response), 201



@topics.route('/topics/<topic_slug>', methods=['GET', 'DELETE'])
def topic_detail(topic_slug):

    topic = Topic.get_by_slug(topic_slug)
    if not topic:
        return '', 404

    if request.method == 'GET':
        response = topic_detail_serializer(topic)
        return jsonify(response) 

    if request.method == 'DELETE':
        topic.delete()
        return '', 204
