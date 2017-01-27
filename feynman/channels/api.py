from flask import request
from flask import jsonify
from .models import Channel
from . import channels



@channels.route('/channels', methods=['GET', 'POST'])
def channel_list():

    if request.method == 'GET':
        channels = Channel.get_all()
        response = Channel.serialize_list(channels)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        channel = Channel(data)
        channel.save()
        response = channel.serialize()
        return jsonify(response), 201



@channels.route('/channels/<channel_slug>', methods=['GET', 'DELETE'])
def channel_detail(channel_slug):

    if request.method == 'GET':
        channel = Channel.get_by_slug(channel_slug)
        if channel:
            response = channel.serialize()
            return jsonify(response) 
        return '', 404

    if request.method == 'DELETE':
        channel = Channel.get_by_slug(channel_slug)
        if channel:
            channel.delete()
            return '', 204
        return '', 404
