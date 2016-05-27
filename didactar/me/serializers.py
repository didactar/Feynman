from flask import jsonify

from didactar.users.models import User


def settings_dict(user):
    return {
        'id': user.id, 
        'username': user.username, 
        'name': user.name,
        'avatar': user.avatar,
        'about': user.about,
        'language': 'EN',
        'timezone': 'x',
        'email': 'asimov@didactar.com',
        'emailFrequency': 'daily'
    }

def settings_serializer():
    user = User.get_by_username('isaac-asimov')
    user_settings = settings_dict(user)
    return jsonify(user_settings)


def preferences_dict(user):
    return {
        'username': user.username, 
        'name': user.name,
        'avatar': user.avatar,
        'language': 'EN',
        'timezone': 'x'
    }

def preferences_serializer():
    user = User.get_by_username('isaac-asimov')
    preferences = preferences_dict(user)
    return jsonify(preferences)
