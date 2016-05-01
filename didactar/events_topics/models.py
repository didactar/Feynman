from didactar.database import db

class EventTopic(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __init__(self, event_slug, topic_slug):
        self.event = event_slug
        self.topic = topic_slug

    @classmethod
    def create(self, event_slug='', topic_slug=''):
        event_topic = EventTopic(event_slug, topic_slug)
        db.session.add(event_topic)
        db.session.commit()
        return event_topic

    @classmethod
    def get(self, event_slug='', topic_slug=''):
        event_id = Event.get(event_slug).id
        topic_id = Topic.get(topic_slug).id
        return EventTopic.query.filter_by(
                    event_id=event_id, 
                    topic_slug=topic_slug).first()

    @classmethod
    def filter_by_event(self, event_slug=''):
        event_id = Event.get(event_slug).id
        return EventTopic.query.filter_by(event_id=event_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
