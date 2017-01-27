from flask import jsonify
from flask import request
from .models import Event
from feynman.channels.models import Channel
from . import events



@events.route('/events', methods=['GET', 'POST'])
def event_list():

    if request.method == 'GET':
        events = Event.get_all()
        response = Event.serialize_list(events)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        event = Event(data)
        event.save()
        response = event.serialize()
        return jsonify(response), 201



@events.route('/events/<event_slug>', methods=['GET', 'DELETE'])
def event_detail(event_slug):

    if request.method == 'GET':
        event = Event.get_by_slug(event_slug)
        if event:
            response = event.serialize()
            return jsonify(response) 
        return '', 404

    if request.method == 'DELETE':
        event = Event.get_by_slug(event_slug)
        if event:
            event.delete()
            return '', 204
        return '', 404



@events.route('/channels/<channel_slug>/events', methods=['GET'])
def channel_event_list(channel_slug):

    if request.method == 'GET':
        channel = Channel.get_by_slug(channel_slug)
        if channel:
            response = Event.serialize_list(channel.events)
            return jsonify(response)
        return '', 404
