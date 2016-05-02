import json
from flask import Blueprint
from flask import request

from .models import Marking
from .serializers import marking_detail_serializer
from .serializers import marking_list_serializer

markings = Blueprint('markings', __name__)


@markings.route('/markings', methods=['POST'])
def marking_list():
    try: 
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        marking = Marking(data)
        marking.save()
        return marking_detail_serializer(marking), 201
    except:
        return '', 400


@markings.route('/markings/<id>', methods=['GET', 'DELETE'])
def marking_detail(id):

    if request.method == 'GET':
        marking = Marking.get(id)
        if not marking:
            return '', 404
        return marking_detail_serializer(marking), 200

    if request.method == 'DELETE':
        marking = Marking.get(id)
        if not marking:
            return '', 404
        marking.delete()
        return '', 204


@markings.route('/topics/<topic_slug>/markings', methods=['GET'])
def topic_markings(topic_slug):
    marking_list = Marking.filter_by_topic(topic_slug)
    if not marking_list:
        return '', 400
    return marking_list_serializer(marking_list), 200


@markings.route('/events/<event_slug>/markings', methods=['GET'])
def event_markings(event_slug):
    marking_list = Marking.filter_by_event(event_slug)
    if not marking_list:
        return '', 400
    return marking_list_serializer(marking_list), 200
