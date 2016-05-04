import json
from flask import Blueprint
from flask import request

from .models import Event
from .serializers import detail_serializer
from .serializers import list_serializer

events = Blueprint('events', __name__)


@events.route('/events', methods=['GET', 'POST'])
def event_list():

    if request.method == 'GET':
        events = Event.all()
        return list_serializer(events)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))
            event = Event(data)
            event.save()
            return detail_serializer(event), 201
        except:
            return '', 400


@events.route('/events/<slug>', methods=['GET', 'DELETE'])
def event_detail(slug):

    if request.method == 'GET':
        try:
            event = Event.get_by_slug(slug)
            if not event:
                return '', 404
            return detail_serializer(event), 200
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
