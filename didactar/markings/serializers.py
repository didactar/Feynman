from flask import jsonify

def serializer(marking):
    
    event = marking.get_event()
    topic = marking.get_topic()

    return {
        'id': marking.id,
        'event': {
            'id': event.id,
            'slug': event.slug,
            'title': event.title
        },
        'topic': {
            'id': topic.id,
            'slug': topic.slug,
            'name': topic.name
        }
    }


def marking_detail_serializer(marking):
    s = serializer(marking)
    return jsonify(s)


def marking_list_serializer(markings):
    data = [serializer(m) for m in markings]
    return jsonify(data=data)
