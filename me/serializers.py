from flask import jsonify

def preferences():
    return {
        'language': 'EN',
        'timezone': 'x'
    }

def preferences_serializer():
    return jsonify(preferences())
