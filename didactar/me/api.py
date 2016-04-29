import json
from flask import Blueprint
from flask import request

from .serializers import preferences_serializer

me = Blueprint('me', __name__)


@me.route('/api/v1/me/preferences', methods=['GET'])
def preferences():

    if request.method == 'GET':
        return preferences_serializer()
