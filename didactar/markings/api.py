import json
from flask import Blueprint
from flask import request
from flask import jsonify

from didactar.topics.models import Topic
from didactar.events.models import Event
from .models import Marking

from .serializers import marking_detail_serializer
from .serializers import event_marking_list_serializer
from .serializers import topic_marking_list_serializer


markings = Blueprint('markings', __name__)


@markings.route('/markings', methods=['POST'])
def marking_list():

    if request.method == 'POST':
        data = request.get_json()
        marking = Marking(data)
        marking.save()
        response = marking_detail_serializer(marking)
        return jsonify(response), 201 


@markings.route('/markings/<id>', methods=['GET', 'DELETE'])
def marking_detail(id):

    marking = Marking.get_by_id(id)
    if not marking:
        return '', 404

    if request.method == 'GET':
        response = marking_detail_serializer(marking)
        return jsonify(response)

    if request.method == 'DELETE':
        marking.delete()
        return '', 204


@markings.route('/events/<event_slug>/markings', methods=['GET'])
def event_marking_list(event_slug):

    event = Event.get_by_slug(event_slug)
    if not event:
        return '', 404

    if request.method == 'GET':
        response = event_marking_list_serializer(event.markings)
        return jsonify(response) 


@markings.route('/topics/<topic_slug>/markings', methods=['GET'])
def topic_marking_list(topic_slug):

    topic = Topic.get_by_slug(topic_slug)
    if not topic:
        return '', 404

    if request.method == 'GET':
        response = topic_marking_list_serializer(topic.markings)
        return jsonify(response)
