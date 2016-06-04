from slugify import slugify
from database import db

class Topic(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    description = db.Column(db.Text)
    image = db.Column(db.String(512))
    slug = db.Column(db.String(1024))
    markings = db.relationship('Marking', backref='topic', lazy='dynamic')

    def __init__(self, data):
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.image = data.get('image', '')
        self.slug = slugify(data.get('name'), to_lower=True)

    @classmethod
    def get_all(self):
        return Topic.query.all()

    @classmethod
    def get_by_slug(self, slug):
        return Topic.query.filter_by(slug=slug).first()
    
    @classmethod
    def get_by_id(self, id):
        return Topic.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
