import json
from flask import Blueprint
from flask import request

from didactar.users.models import User
from didactar.events.models import Event

from .models import Speakership
from .serializers import detail_serializer
from .serializers import list_serializer_user
from .serializers import list_serializer_event


speakerships = Blueprint('speakerships', __name__)


@speakerships.route('/speakerships', methods=['POST'])
def speakership_list():
    try:
        request_content = request.data.decode('utf-8')
        data = json.loads(request_content)
        speakership = Speakership(data)
        speakership.save()
        return detail_serializer(speakership), 201
    except:
        return '', 400


@speakerships.route('/speakerships/<id>', methods=['GET', 'DELETE'])
def speakership_detail(id):

    if request.method == 'GET':
        try:
            speakership = Speakership.get(id)
            if not speakership:
                return '', 404
            return detail_serializer(speakership), 200
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            speakership = Speakership.get(id)
            if not speakership:
                return '', 404
            speakership.delete()
            return '', 204
        except:
            return '', 400


@speakerships.route('/users/<username>/speakerships', methods=['GET'])
def user_speakerships(username):
    try:
        user = User.get_by_username(username)
        if not user:
            return '', 404
        speakerships = Speakership.filter_by_user(user)
        return list_serializer_event(speakerships)
    except:
        return '', 400



@speakerships.route('/events/<event_slug>/speakerships', methods=['GET'])
def event_speakerships(event_slug):
    try:
        event = Event.get_by_slug(event_slug)
        if not event:
            return '', 404
        markings = Speakership.filter_by_event(event)
        return list_serializer_user(markings), 200
    except:
        return '', 400
