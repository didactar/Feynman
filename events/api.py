import json
from flask import Blueprint
from flask import jsonify
from flask import request
from .models import Event

events = Blueprint('events', __name__)


@events.route('/events', methods=['POST'])
def event_list():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        title = data['title']
        event = Event.new(title)
        return jsonify(title=event.title), 201
