from database import db
from slugify import slugify

class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    slug = db.Column(db.String(1024))

    def __init__(self, title):
        self.title = title
        self.slug = slugify(title, to_lower=True)

    @classmethod
    def all(self):
        return Event.query.all()

    @classmethod
    def new(self, title):
        event = Event(title)
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
