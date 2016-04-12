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
        data = json.loads(request.data.decode('utf-8'))
        title = data['title']
        event = Event.new(title)
        return event_detail_serializer(event), 201
