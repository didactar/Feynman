import json
from flask import Blueprint
from flask import request

from .models import Participation
from .serializers import participation_detail_serializer
from .serializers import participation_list_serializer

participations = Blueprint('participations', __name__)


@participations.route('/participations', methods=['POST'])
def participation_list():
    try: 
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        participation = Participation(data)
        participation.save()
        return participation_detail_serializer(participation), 201
    except:
        return '', 400


@participations.route('/participations/<id>', methods=['GET', 'DELETE'])
def participation_detail(id):

    if request.method == 'GET':
        participation = Participation.get(id)
        if not participation:
            return '', 404
        return participation_detail_serializer(participation), 200

    if request.method == 'DELETE':
        participation = Participation.get(id)
        if not participation:
            return '', 404
        participation.delete()
        return '', 204


@participations.route('/events/<event_slug>/participations', methods=['GET'])
def event_participations(event_slug):
    participations = Participation.filter_by_event(event_slug)
    if not participations:
        return '', 400
    return participation_list_serializer(participations)


@participations.route('/users/<username>/participations', methods=['GET'])
def user_participations(username):
    participations = Participation.filter_by_user(username)
    if not participations:
        return '', 400
    return participation_list_serializer(participations)
