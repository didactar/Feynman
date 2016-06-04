import json
from flask import Blueprint
from flask import request
from flask import jsonify

from didactar.users.models import User
from didactar.channels.models import Channel
from didactar.events.models import Event
from .models import Participation

from .serializers import participation_serializer
from .serializers import user_participation_list_serializer
from .serializers import event_participation_list_serializer


participations = Blueprint('participations', __name__)


@participations.route('/participations', methods=['POST'])
def participation_list():

    if request.method == 'POST':
        data = request.get_json()
        participation = Participation(data)
        participation.save()
        response = participation_serializer(participation)
        return jsonify(response), 201



@participations.route('/participations/<id>', methods=['GET', 'DELETE'])
def participation_detail(id):

    participation = Participation.get_by_id(id)
    if not participation:
        return '', 404

    if request.method == 'GET':
        response = participation_serializer(participation)
        return jsonify(response)

    if request.method == 'DELETE':
        participation.delete()
        return '', 204


@participations.route('/events/<event_slug>/participations', methods=['GET'])
def event_participation_list(event_slug):

    event = Event.get_by_slug(event_slug)
    if not event:
        return '', 404

    if request.method == 'GET':
        response = event_participation_list_serializer(event.participations)
        return jsonify(response)


@participations.route('/users/<username>/participations', methods=['GET'])
def user_participation_list(username):

    user = User.get_by_username(username)
    if not user:
        return '', 404

    if request.method == 'GET':
        channel_slug = request.args.get('channel')
        if channel_slug:
            channel = Channel.get_by_slug(channel_slug)
            if not channel:
                return '', 404
            participations = user.get_channel_participations(channel)
        if not channel_slug:
            participations = user.participations
        response = user_participation_list_serializer(participations)
        return jsonify(response)
