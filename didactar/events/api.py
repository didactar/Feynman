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
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        event = Event.create(data)
        return event_detail_serializer(event), 201



@events.route('/events/<slug>', methods=['GET', 'DELETE'])
def event_detail(slug):

    if request.method == 'GET':
        event = Event.get(slug)
        if not event:
            return '', 404
        return event_detail_serializer(event), 200

    if request.method == 'DELETE':
        event = Event.get(slug)
        if not event:
            return '', 404
        event.delete()
        return '', 204
