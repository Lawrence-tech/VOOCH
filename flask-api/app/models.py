from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    reviewer_privileges = db.Column(db.Boolean, default=False)
    artworks = db.relationship('Artwork', backref='uploader', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name
        }
        return data

    def from_dict(self, data):
        for field in ['username', 'email', 'name', 'password']:
            if field in data:
                setattr(self, field, data[field])

    def set_password(self, password):
        """implement password hashing"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Performs verification takes password hash
        and password entered by user at time of login"""
        return check_password_hash(self.password_hash, password)

    # implement the is_reviwer property
    @property
    def is_reviewer(self):
        """Checks if its a reviewer"""
        return self.reviewer_privileges


class Reviewer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    artworks = db.relationship('Artwork', backref='uploader', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name
        }
        return data

    def from_dict(self, data):
        for field in ['username', 'email', 'name', 'password']:
            if field in data:
                setattr(self, field, data[field])

    def set_password(self, password):
        """implement password hashing"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Performs verification takes password hash
        and password entered by reviewer at time of login"""
        return check_password_hash(self.password_hash, password)


class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    image = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Artwork {self.title}>'


@login.user_loader
def load_user(user_id):
    """Load a user/reviwer given the ID"""
    user = User.query.get(int(user_id))
    if user:
        return user

    # if the user with given ID is not a regular user, try loading a reviwer
    reviewer = Reviewer.query.get(int(user_id))
    if reviewer:
        return reviewer

    # if neither a user nor a reviwer is found with given ID
    return None
