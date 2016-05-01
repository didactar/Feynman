import json
from flask import Blueprint
from flask import request

from .models import Marking
from .serializers import marking_detail_serializer
from .serializers import marking_list_serializer

markings = Blueprint('markings', __name__)


@markings.route('/events/<event_slug>/topics', methods=['GET', 'POST'])
def markings_list(event_slug):

    if request.method == 'GET':
        marking_list = Marking.filter_by_event(event_slug)
        if not marking_list:
            return '', 400
        return marking_list_serializer(marking_list)
    
    if request.method == 'POST':
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        topic_slug = data['slug']
        marking = Marking.create(event_slug, topic_slug)
        if not marking:
            return '', 400
        return marking_detail_serializer(marking), 201


@markings.route('/topics/<topic_slug>/events', methods=['GET'])
def topic_events_list(topic_slug):

    if request.method == 'GET':
        marking_list = Marking.filter_by_topic(topic_slug)
        if not marking_list:
            return '', 400
        return marking_list_serializer(marking_list)


@markings.route('/events/<event_slug>/topics/<topic_slug>', methods=['GET', 'DELETE'])
def marking_detail(event_slug, topic_slug):

    if request.method == 'GET':
        marking = Marking.get(event_slug, topic_slug)
        if not marking:
            return '', 404
        return marking_detail_serializer(marking), 200

    if request.method == 'DELETE':
        marking = Marking.get(event_slug, topic_slug)
        if not marking:
            return '', 404
        marking.delete()
        return '', 204
