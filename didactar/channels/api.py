from flask import Blueprint
from flask import request
from flask import jsonify
from flask import url_for

from .models import Channel

from .serializers import channel_detail_serializer
from .serializers import channel_list_serializer


channels = Blueprint('channels', __name__)


@channels.route('/channels', methods=['GET', 'POST'])
def channel_list():

    if request.method == 'GET':
        channels = Channel.get_all()
        response = channel_list_serializer(channels)
        return jsonify(response)

    if request.method == 'POST':
        data = request.get_json()
        channel = Channel(data)
        channel.save()
        response = channel_detail_serializer(channel)
        return jsonify(response), 201



@channels.route('/channels/<channel_slug>', methods=['GET', 'DELETE'])
def channel_detail(channel_slug):

    channel = Channel.get_by_slug(channel_slug)
    if not channel:
        return '', 404

    if request.method == 'GET':
        response = channel_detail_serializer(channel)
        return jsonify(response) 

    if request.method == 'DELETE':
        channel.delete()
        return '', 204
