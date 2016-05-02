import json
from flask import Blueprint
from flask import request

from .models import User
from .serializers import user_detail_serializer
from .serializers import user_list_serializer

users = Blueprint('users', __name__)


@users.route('/users', methods=['GET', 'POST'])
def user_list():

    if request.method == 'GET':
        users = User.all()
        return user_list_serializer(users)
    
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        try:
            user = User(data)
            user.save()
            return user_detail_serializer(user), 201
        except:
            return '', 400 



@users.route('/users/<username>', methods=['GET', 'DELETE'])
def user_detail(username):

    if request.method == 'GET':
        try:
            user = User.get(username)
            return user_detail_serializer(user), 200
        except:
            return '', 404

    if request.method == 'DELETE':
        try:
            user = User.get(username)
            user.delete()
            return '', 204
        except:
            return '', 404
