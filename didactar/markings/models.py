from didactar.database import db


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
    def filter_by_event(self, event):
        return Marking.query.filter_by(event_id=event.id)

    @classmethod
    def filter_by_topic(self, topic):
        return Marking.query.filter_by(topic_id=topic.id)

    def get_event_id(self):
        return self.event_id

    def get_topic_id(self):
        return self.topic_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
