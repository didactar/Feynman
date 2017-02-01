from flask import request
from flask import jsonify
from feynman.users.models import User
from feynman.workshops.models import Workshop
from feynman.events.models import Event
from .models import Participation
from . import participations



@participations.route('/participations', methods=['POST'])
def participation_list():

    if request.method == 'POST':
        data = request.get_json()
        participation = Participation(data)
        participation.save()
        response = participation.serialize()
        return jsonify(response), 201



@participations.route('/participations/<id>', methods=['GET', 'DELETE'])
def participation_detail(id):

    if request.method == 'GET':
        participation = Participation.get_by_id(id)
        if participation:
            response = participation.serialize()
            return jsonify(response)
        return '', 404

    if request.method == 'DELETE':
        participation = Participation.get_by_id(id)
        if participation:
            participation.delete()
            return '', 204
        return '', 404



@participations.route('/events/<event_slug>/participations', methods=['GET'])
def event_participation_list(event_slug):

    if request.method == 'GET':
        event = Event.get_by_slug(event_slug)
        if event:
            response = Participation.serialize_event_participations_list(event.participations)
            return jsonify(response)
        return '', 404



@participations.route('/users/<username>/participations', methods=['GET'])
def user_participation_list(username):

    if request.method == 'GET':
        user = User.get_by_username(username)
        if user:
            workshop_slug = request.args.get('workshop')
            workshop = Workshop.get_by_slug(workshop_slug) if workshop_slug else None
            participations = user.get_participations(workshop)
            response = Participation.serialize_user_participations_list(participations)
            return jsonify(response)
        return '', 404
