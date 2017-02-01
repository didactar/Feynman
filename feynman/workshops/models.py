from slugify import slugify
from database import db


class Workshop(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    description = db.Column(db.Text)
    image = db.Column(db.String(512))
    avatar = db.Column(db.String(512))
    slug = db.Column(db.String(1024))
    events = db.relationship('Event', backref='workshop', lazy='dynamic')

    def __init__(self, data):
        self.name = data.get('name', '')
        self.description = data.get('description', '')
        self.image = data.get('image', '')
        self.avatar = data.get('avatar', '')
        self.slug = slugify(data.get('name'))

    @classmethod
    def get_all(self):
        return Workshop.query.all()

    @classmethod
    def get_by_slug(self, slug):
        return Workshop.query.filter_by(slug=slug).first()
    
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
            'slug': self.slug,
            'image': self.image,
            'avatar': self.avatar,
            'description': self.description
        }

    @classmethod
    def serialize_list(self, workshops):
        return {
            'data': [workshop.serialize() for workshop in workshops]
        }
