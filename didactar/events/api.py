import json
from flask import jsonify
from flask import Blueprint
from flask import request

from didactar.channels.models import Channel
from .models import Event

from .serializers import event_detail_serializer
from .serializers import event_list_serializer


events = Blueprint('events', __name__)


@events.route('/events', methods=['POST'])
def event_list():

    if request.method == 'POST':
        data = request.get_json()
        event = Event(data)
        event.save()
        response = event_detail_serializer(event)
        return jsonify(response), 201


@events.route('/events/<event_slug>', methods=['GET', 'DELETE'])
def event_detail(event_slug):

    event = Event.get_by_slug(event_slug)
    if not event:
        return '', 404

    if request.method == 'GET':
        response = event_detail_serializer(event)
        return jsonify(response) 

    if request.method == 'DELETE':
        event.delete()
        return '', 204


@events.route('/channels/<channel_slug>/events', methods=['GET'])
def channel_event_list(channel_slug):

    channel = Channel.get_by_slug(channel_slug)
    if not channel:
        return '', 404

    if request.method == 'GET':
        response = event_list_serializer(channel.events)
        return jsonify(response)
