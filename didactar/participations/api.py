import json
from flask import Blueprint
from flask import request

from didactar.events.models import Event
from didactar.users.models import User

from .models import Participation
from .serializers import detail_serializer
from .serializers import list_serializer_user
from .serializers import list_serializer_event


participations = Blueprint('participations', __name__)


@participations.route('/participations', methods=['POST'])
def participation_list():
    try:
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        participation = Participation(data)
        participation.save()
        return detail_serializer(participation), 201
    except:
        return '', 400


@participations.route('/participations/<id>', methods=['GET', 'DELETE'])
def participation_detail(id):

    if request.method == 'GET':
        try:
            participation = Participation.get(id)
            if not participation:
                return '', 404
            return detail_serializer(participation), 200
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            participation = Participation.get(id)
            if not participation:
                return '', 404
            participation.delete()
            return '', 204
        except:
            return '', 400


@participations.route('/events/<event_slug>/participations', methods=['GET'])
def event_participations(event_slug):
    try:
        event = Event.get_by_slug(event_slug)
        if not event:
            return '', 404
        participations = Participation.filter_by_event(event)
        return list_serializer_user(participations)
    except:
        return '', 400


@participations.route('/users/<username>/participations', methods=['GET'])
def user_participations(username):
    try:
        user = User.get_by_username(username)
        if not user:
            return '', 404
        participations = Participation.filter_by_user(user)
        return list_serializer_event(participations)
    except:
        return '', 400
