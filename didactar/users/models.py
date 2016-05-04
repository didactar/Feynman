from slugify import slugify
from didactar.database import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    username = db.Column(db.String(512))
    avatar = db.Column(db.String(512))
    about = db.Column(db.Text)

    def __init__(self, data):
        self.name = data['name']
        self.avatar = data['avatar']
        self.about = data['about']
        self.username = slugify(data['name'], to_lower=True)

    @classmethod
    def all(cls):
        return User.query.all()

    @classmethod
    def get_by_username(cls, username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def get_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
