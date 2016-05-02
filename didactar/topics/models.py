from slugify import slugify
from didactar.database import db

class Topic(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    description = db.Column(db.Text)
    slug = db.Column(db.String(1024))

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.slug = slugify(name, to_lower=True)

    @classmethod
    def all(self):
        return Topic.query.all()

    @classmethod
    def new(self, name, description):
        topic = Topic(name, description)
        db.session.add(topic)
        db.session.commit()
        return topic

    @classmethod
    def get(self, slug):
        return Topic.query.filter_by(slug=slug).first()
    
    @classmethod
    def get_by_id(self, id):
        return Topic.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
