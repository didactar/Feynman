from database import db
from slugify import slugify

class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    description = db.Column(db.Text)
    slug = db.Column(db.String(1024))

    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.slug = slugify(title, to_lower=True)

    @classmethod
    def all(self):
        return Event.query.all()

    @classmethod
    def new(self, title, description):
        event = Event(title, description)
        db.session.add(event)
        db.session.commit()
        return event

    @classmethod
    def get(self, slug):
        return Event.query.filter_by(slug=slug).first()

    @classmethod
    def delete(self, slug):
        event = Event.get(slug)
        db.session.delete(event)
        db.session.commit()

    @classmethod
    def filterByTopic(self, topic):
        return Event.query.filter_by(topic=topic)
