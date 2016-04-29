from flask import jsonify

def event_serializer(event):
    return {
        'title': event.title, 
        'slug': event.slug,
        'description': event.description
    }

def event_detail_serializer(event):
    return jsonify(event_serializer(event))

def event_list_serializer(events):
    data = [event_serializer(event) for event in events]
    return jsonify(data=data)
