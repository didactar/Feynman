from flask import Blueprint
from flask import request
from flask import jsonify
from flask import url_for

from .models import User

from .serializers import user_detail_serializer
from .serializers import user_list_serializer


users = Blueprint('users', __name__)


@users.route('/users', methods=['GET', 'POST'])
def user_list():

    if request.method == 'GET':
        users = User.get_all()
        response = user_list_serializer(users)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        user = User(data)
        user.save()
        response = user_detail_serializer(user)
        return jsonify(response), 201



@users.route('/users/<username>', methods=['GET', 'DELETE'])
def user_detail(username):

    user = User.get_by_username(username)
    if not user:
        return '', 404

    if request.method == 'GET':
        response = user_detail_serializer(user)
        return jsonify(response) 

    if request.method == 'DELETE':
        user.delete()
        return '', 204
