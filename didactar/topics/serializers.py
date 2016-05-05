from flask import jsonify

def topic_dict(topic):
    return {
        'id': topic.id, 
        'name': topic.name, 
        'slug': topic.slug,
        'image': topic.image,
        'description': topic.description
    }


def detail_serializer(topic):
    d = topic_dict(topic)
    return jsonify(d)


def list_serializer(topics):
    d = [topic_dict(topic) for topic in topics]
    return jsonify(data=d)
