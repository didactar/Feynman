from didactar.database import db
from didactar.events.models import Event
from didactar.topics.models import Topic

class EventTopic(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __init__(self, event_id, topic_id):
        self.event_id = event_id
        self.topic_id = topic_id

    @classmethod
    def create(self, event_slug, topic_slug):
        event_id = Event.get(event_slug).id
        topic_id = Topic.get(topic_slug).id
        event_topic = EventTopic(event_id, topic_id)
        db.session.add(event_topic)
        db.session.commit()
        return event_topic

    @classmethod
    def get(self, event_slug, topic_slug):
        event_id = Event.get(event_slug).id
        topic_id = Topic.get(topic_slug).id
        return EventTopic.query.filter_by(
                    event_id=event_id, 
                    topic_id=topic_id).first()

    @classmethod
    def filter_by_event(self, event_slug=''):
        event_id = Event.get(event_slug).id
        return EventTopic.query.filter_by(event_id=event_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
