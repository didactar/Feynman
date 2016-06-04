def user_detail_serializer(user):
    return {
        'id': user.id, 
        'name': user.name, 
        'username': user.username,
        'avatar': user.avatar,
        'about': user.about
    }


def user_list_serializer(users):
    return {
        'data': [{
            'id': user.id, 
            'name': user.name, 
            'username': user.username,
            'avatar': user.avatar,
            'about': user.about
        } for user in users]
    }
