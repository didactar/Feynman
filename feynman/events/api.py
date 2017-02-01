from flask import jsonify
from flask import request
from .models import Event
from feynman.workshops.models import Workshop
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



@events.route('/workshops/<workshop_slug>/events', methods=['GET'])
def workshop_event_list(workshop_slug):

    if request.method == 'GET':
        workshop = Workshop.get_by_slug(workshop_slug)
        if workshop:
            response = Event.serialize_list(workshop.events)
            return jsonify(response)
        return '', 404
