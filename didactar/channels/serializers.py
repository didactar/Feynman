from flask import jsonify

def channel_dict(channel):
    return {
        'id': channel.id, 
        'name': channel.name, 
        'slug': channel.slug,
        'image': channel.image,
        'description': channel.description
    }


def detail_serializer(channel):
    d = channel_dict(channel)
    return jsonify(d)


def list_serializer(channels):
    d = [channel_dict(channel) for channel in channels]
    return jsonify(data=d)
