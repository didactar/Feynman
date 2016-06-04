def topic_detail_serializer(topic):
    return {
        'id': topic.id, 
        'name': topic.name, 
        'slug': topic.slug,
        'image': topic.image,
        'description': topic.description
    }


def topic_list_serializer(topics):
    return {
        'data': [{
            'id': topic.id, 
            'name': topic.name, 
            'slug': topic.slug,
            'image': topic.image,
            'description': topic.description
        } for topic in topics]
    }
