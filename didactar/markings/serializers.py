def marking_detail_serializer(marking):
    return {
        'id': marking.id,
        'event': {'id': marking.event.id},
        'topic': {'id': marking.topic.id}
    }


def event_marking_list_serializer(markings):
    return {
        'data': [{
            'id': m.id,
            'topic': {
                'id': m.topic.id,
                'name': m.topic.name,
                'description': m.topic.description,
                'slug': m.topic.slug,
                'image': m.topic.image
            } 
        } for m in markings]
    }


def topic_marking_list_serializer(markings):
    return {
        'data': [{
            'id': m.id,
            'event': {
                'id': m.event.id, 
                'title': m.event.title, 
                'slug': m.event.slug,
                'channel': {
                    'id': m.event.channel.id,
                    'slug': m.event.channel.slug,
                    'name': m.event.channel.name,
                    'avatar': m.event.channel.avatar
                },
                'description': m.event.description,
                'participationCount': m.event.participations_count
            } 
        } for m in markings]
    }
