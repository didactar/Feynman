from flask import request
from flask import jsonify
from .models import User
from . import users



@users.route('/users', methods=['GET', 'POST'])
def user_list():

    if request.method == 'GET':
        users = User.get_all()
        response = User.serialize_list(users)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        user = User(data)
        user.save()
        response = user.serialize()
        return jsonify(response), 201



@users.route('/users/<username>', methods=['GET', 'DELETE'])
def user_detail(username):

    if request.method == 'GET':
        user = User.get_by_username(username)
        if user:
            response = user.serialize()
            return jsonify(response) 
        return '', 404

    if request.method == 'DELETE':
        user = User.get_by_username(username)
        if user:
            user.delete()
            return '', 204
        return '', 404
