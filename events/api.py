import json
from flask import Blueprint
from flask import request
from .models import Event
from .serializers import event_detail_serializer
from .serializers import event_list_serializer


events = Blueprint('events', __name__)


@events.route('/api/v1/events', methods=['GET', 'POST'])
def event_list():

    if request.method == 'GET':
        events = Event.all()
        return event_list_serializer(events)
    
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        title = data['title']
        description = data['description']
        event = Event.new(title, description)
        return event_detail_serializer(event), 201



@events.route('/api/v1/events/<slug>', methods=['GET', 'DELETE'])
def event_detail(slug):

    if request.method == 'GET':
        event = Event.get(slug)
        if event:
            return event_detail_serializer(event), 200
        else:
            return '', 404

    if request.method == 'DELETE':
        event = Event.get(slug)
        if event:
            Event.delete(slug)
            return '', 204
        else:
            return '', 404
