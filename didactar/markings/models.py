from didactar.database import db
from didactar.events.models import Event
from didactar.topics.models import Topic


class Marking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __init__(self, data):
        self.event_id = data['event']['id']
        self.topic_id = data['topic']['id']

    @classmethod
    def get(self, id):
        return Marking.query.filter_by(id=id).first()

    @classmethod
    def filter_by_event(self, event_slug):
        event_id = Event.get(event_slug).id
        return Marking.query.filter_by(event_id=event_id)

    @classmethod
    def filter_by_topic(self, topic_slug):
        topic_id = Topic.get(topic_slug).id
        return Marking.query.filter_by(topic_id=topic_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
