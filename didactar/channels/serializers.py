def channel_detail_serializer(channel):
    return {
        'id': channel.id, 
        'name': channel.name, 
        'slug': channel.slug,
        'image': channel.image,
        'description': channel.description
    }


def channel_list_serializer(channels):
    return {
        'data': [{
            'id': channel.id, 
            'name': channel.name, 
            'slug': channel.slug,
            'image': channel.image,
            'description': channel.description
        } for channel in channels]
    }
