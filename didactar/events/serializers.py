def event_detail_serializer(event):
    return {
        'id': event.id, 
        'title': event.title, 
        'slug': event.slug,
        'channel': {
            'id': event.channel.id,
            'slug': event.channel.slug,
            'name': event.channel.name,
            'avatar': event.channel.avatar
        },
        'description': event.description,
        'participationCount': event.participations_count,
        'hosts': [{
            'id': s.id,
            'user': {
                'username': s.user.username,
                'name': s.user.name,
                'about': s.user.about,
                'avatar': s.user.avatar
            }
        } for s in event.hostings]
    }


def event_list_serializer(events):
    return {
        'data': [{
            'id': event.id, 
            'title': event.title, 
            'slug': event.slug,
            'channel': {
                'id': event.channel.id,
                'slug': event.channel.slug,
                'name': event.channel.name,
                'avatar': event.channel.avatar
            },
            'description': event.description,
            'participationCount': event.participations_count,
            'hosts': [{
                'id': s.id,
                'user': {
                    'username': s.user.username,
                    'name': s.user.name,
                    'about': s.user.about,
                    'avatar': s.user.avatar
                }
            } for s in event.hostings]
        } for event in events]
    }
