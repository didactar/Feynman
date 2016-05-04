import json
from flask import Blueprint
from flask import request

from .models import Event
from .serializers import event_detail_serializer
from .serializers import event_list_serializer

events = Blueprint('events', __name__)


@events.route('/events', methods=['GET', 'POST'])
def event_list():

    if request.method == 'GET':
        events = Event.all()
        return event_list_serializer(events)
    
    if request.method == 'POST':
        try:
            request_content = request.data.decode('utf-8')
            data = json.loads(request_content)
            event = Event.create(data)
            return event_detail_serializer(event), 201
        except:
            return '', 400


@events.route('/events/<slug>', methods=['GET', 'DELETE'])
def event_detail(slug):

    if request.method == 'GET':
        try:
            event = Event.get_by_slug(slug)
            if not event:
                return '', 404
            return event_detail_serializer(event), 200
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            event = Event.get(slug)
            if not event:
                return '', 404
            event.delete()
            return '', 204
        except:
            return '', 400
