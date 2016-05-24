import json
from flask import Blueprint
from flask import request

from .models import Channel
from .serializers import detail_serializer
from .serializers import list_serializer


channels = Blueprint('channels', __name__)


@channels.route('/channels', methods=['GET', 'POST'])
def channel_list():

    if request.method == 'GET':
        try:
            channels = Channel.all()
            return list_serializer(channels)
        except:
            return '', 400 
    
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))
            channel = Channel(data)
            channel.save()
            return detail_serializer(channel), 201
        except:
            return '', 400 


@channels.route('/channels/<channel_slug>', methods=['GET', 'DELETE'])
def channel_detail(channel_slug):

    if request.method == 'GET':
        try:
            channel = Channel.get_by_slug(channel_slug)
            if not channel:
                return '', 404
            return detail_serializer(channel)
        except:
            return '', 400

    if request.method == 'DELETE':
        try:
            channel = Channel.get_by_slug(channel_slug)
            if not channel:
                return '', 404
            channel.delete()
            return '', 204
        except:
            return '', 400
