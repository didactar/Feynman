import json
from flask import Blueprint
from flask import request

from .serializers import settings_serializer
from .serializers import preferences_serializer


me = Blueprint('me', __name__)


@me.route('/me/settings', methods=['GET'])
def settings():
    return settings_serializer()


@me.route('/me/preferences', methods=['GET'])
def preferences():
    return preferences_serializer()
