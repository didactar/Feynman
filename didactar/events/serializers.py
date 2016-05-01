from flask import jsonify

def serializer(event):
    return {
        'id': event.id, 
        'title': event.title, 
        'slug': event.slug,
        'description': event.description
    }

def event_detail_serializer(event):
    s = serializer(event)
    return jsonify(s)

def event_list_serializer(events):
    data = [serializer(event) for event in events]
    return jsonify(data=data)
