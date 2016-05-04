from flask import jsonify

def serializer(user):
    return {
        'id': user.id, 
        'username': user.username, 
        'name': user.name,
        'avatar': user.avatar,
        'about': user.about,
        'stats': {
            'speaker': 1,
            'subscriber': 2,
            'moderator': 3,
            'participant': 4
        }
    }

def user_detail_serializer(user):
    s = serializer(user)
    return jsonify(s)

def user_list_serializer(users):
    data = [serializer(user) for user in users]
    return jsonify(data=data)
