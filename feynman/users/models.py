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
        self.username = slugify(data.get('name', ''))

    @classmethod
    def get_all(cls):
        return User.query.all()

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def get_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_participations(self, channel=None):
        if channel:
            return self.participations.join('event', 'channel').filter_by(id=channel.id)
        return self.participations
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'username': self.username,
            'avatar': self.avatar,
            'about': self.about
        }

    @classmethod
    def serialize_list(self, users):
        return {
            'data': [user.serialize() for user in users]
        }

    def settings(self):
        return {
            'id': self.id, 
            'username': self.username, 
            'name': self.name,
            'avatar': self.avatar,
            'about': self.about,
            'language': 'EN',
            'timezone': 'x',
            'email': 'asimov@feynman.com',
            'emailFrequency': 'daily'
        }

    def preferences(self):
        return {
            'username': self.username, 
            'name': self.name,
            'avatar': self.avatar,
            'language': 'EN',
            'timezone': 'x'
        }
