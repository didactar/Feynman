from flask import request
from flask import jsonify
from feynman.users.models import User
from . import me


@me.route('/me/settings', methods=['GET'])
def settings():

    if request.method == 'GET':
        user = User.get_by_username('isaac-asimov')
        settings = user.settings()
        return jsonify(settings)



@me.route('/me/preferences', methods=['GET'])
def preferences():

    if request.method == 'GET':
        user = User.get_by_username('isaac-asimov')
        preferences = user.preferences()
        return jsonify(preferences)
