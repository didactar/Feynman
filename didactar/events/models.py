from slugify import slugify
from didactar.database import db

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
    def create(self, data):
        event = Event(data['title'], data['description'])
        db.session.add(event)
        db.session.commit()
        return event

    @classmethod
    def get(self, event_slug):
        return Event.query.filter_by(slug=event_slug).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
