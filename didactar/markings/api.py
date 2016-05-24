import json
from flask import Blueprint
from flask import request

from didactar.topics.models import Topic
from didactar.events.models import Event

from .models import Marking
from .serializers import detail_serializer
from .serializers import list_serializer_event
from .serializers import list_serializer_topic


markings = Blueprint('markings', __name__)


@markings.route('/markings', methods=['POST'])
def marking_list():
    try: 
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        marking = Marking(data)
        marking.save()
        return detail_serializer(marking), 201
    except:
        return '', 400


@markings.route('/markings/<id>', methods=['GET', 'DELETE'])
def marking_detail(id):

    if request.method == 'GET':
        try:
            marking = Marking.get(id)
            if not marking:
                return '', 404
            return marking_detail_serializer(marking), 200
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            marking = Marking.get(id)
            if not marking:
                return '', 404
            marking.delete()
            return '', 204
        except:
            return '', 400


@markings.route('/topics/<topic_slug>/markings', methods=['GET'])
def topic_markings(topic_slug):
    try:
        topic = Topic.get_by_slug(topic_slug)
        if not topic:
            return '', 404
        markings = Marking.filter_by_topic(topic)
        return list_serializer_event(markings), 200
    except:
        return '', 400



@markings.route('/events/<event_slug>/markings', methods=['GET'])
def event_markings(event_slug):
    try:
        event = Event.get_by_slug(event_slug)
        if not event:
            return '', 404
        markings = Marking.filter_by_event(event)
        return list_serializer_topic(markings), 200
    except:
        return '', 400
