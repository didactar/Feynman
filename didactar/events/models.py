from slugify import slugify
from didactar.database import db

class Event(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512))
    description = db.Column(db.Text)
    slug = db.Column(db.String(1024))
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))

    def __init__(self, data):
        self.title = data.get('title', '')
        self.description = data.get('description', '')
        self.slug = slugify(data.get('title', ''), to_lower=True)
        self.channel_id = data['channel']['id']

    @classmethod
    def all(self):
        return Event.query.all()

    @classmethod
    def get_by_slug(self, event_slug):
        return Event.query.filter_by(slug=event_slug).first()

    @classmethod
    def filter_by_channel(self, channel_id):
        return Event.query.filter_by(channel_id=channel_id)
    
    @classmethod
    def get_by_id(self, id):
        return Event.query.filter_by(id=id).first()
    
    @classmethod
    def get_by_id(self, id):
        return Event.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
