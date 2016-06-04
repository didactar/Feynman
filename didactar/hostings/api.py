import json
from flask import Blueprint
from flask import request
from flask import jsonify

from didactar.users.models import User
from didactar.channels.models import Channel
from didactar.events.models import Event
from .models import Hosting

from .serializers import hosting_serializer
from .serializers import user_hosting_list_serializer
from .serializers import event_hosting_list_serializer


hostings = Blueprint('hostings', __name__)


@hostings.route('/hostings', methods=['POST'])
def hosting_list():

    if request.method == 'POST':
        data = request.get_json()
        hosting = Hosting(data)
        hosting.save()
        response = hosting_serializer(hosting)
        return jsonify(response), 201



@hostings.route('/hostings/<id>', methods=['GET', 'DELETE'])
def hosting_detail(id):

    hosting = Hosting.get_by_id(id)
    if not hosting:
        return '', 404

    if request.method == 'GET':
        response = hosting_serializer(hosting)
        return jsonify(response)

    if request.method == 'DELETE':
        hosting.delete()
        return '', 204


@hostings.route('/events/<event_slug>/hostings', methods=['GET'])
def event_hosting_list(event_slug):

    event = Event.get_by_slug(event_slug)
    if not event:
        return '', 404

    if request.method == 'GET':
        response = event_hosting_list_serializer(event.hostings)
        return jsonify(response)


@hostings.route('/users/<username>/hostings', methods=['GET'])
def user_hosting_list(username):

    user = User.get_by_username(username)
    if not user:
        return '', 404

    if request.method == 'GET':
        channel_slug = request.args.get('channel')
        if channel_slug:
            channel = Channel.get_by_slug(channel_slug)
            if not channel:
                return '', 404
            hostings = user.get_channel_hostings(channel)
        if not channel_slug:
            hostings = user.hostings
        response = user_hosting_list_serializer(hostings)
        return jsonify(response)
