from flask import jsonify

def event_detail_serializer(event):
    return jsonify(title=event.title)

def event_list_serializer(events):
    data = [{'title': event.title} for event in events]
    return jsonify(data=data)
