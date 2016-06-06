from slugify import slugify
from database import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    username = db.Column(db.String(512))
    avatar = db.Column(db.String(512))
    about = db.Column(db.Text)
    participations = db.relationship('Participation', backref='user', lazy='dynamic')

    def __init__(self, data):
        self.name = data.get('name', '')
        self.avatar = data.get('avatar', '')
        self.about = data.get('about', '')
        self.username = slugify(data.get('name', ''), to_lower=True)

    @classmethod
    def get_all(cls):
        return User.query.all()

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def get_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_channel_participations(self, channel):
        return self.participations.join('event', 'channel').filter_by(id=channel.id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
