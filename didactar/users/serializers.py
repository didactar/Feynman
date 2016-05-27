from flask import jsonify

def user_dict(user):
    return {
        'id': user.id, 
        'username': user.username, 
        'name': user.name,
        'avatar': user.avatar,
        'about': user.about,
    }

def user_detail_serializer(user):
    s = user_dict(user)
    return jsonify(s)

def user_list_serializer(users):
    data = [serializer(user) for user in users]
    return jsonify(data=data)
