from slugify import slugify
from database import db


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    slug = db.Column(db.String(1024), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)
    description = db.Column(db.Text)
    participations = db.relationship('Participation', backref='event', lazy='dynamic')

    def __init__(self, event_data):
        self.title = event_data.get('title')
        self.description = event_data.get('description')
        self.slug = slugify(event_data.get('title'), to_lower=True)
        self.channel_id = event_data.get('channel').get('id')

    @classmethod
    def all(self):
        return Event.query.all()

    @classmethod
    def get_by_slug(self, event_slug):
        return Event.query.filter_by(slug=event_slug).first()

    @property
    def participations_count(self):
        return self.participations.count()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
