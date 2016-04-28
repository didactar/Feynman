from flask import jsonify

def topic_serializer(topic):
    return {
        'name': topic.name, 
        'slug': topic.slug,
        'description': topic.description
    }

def topic_detail_serializer(topic):
    return jsonify(topic_serializer(topic))

def topic_list_serializer(topics):
    data = [topic_serializer(topic) for topic in topics]
    return jsonify(data=data)
