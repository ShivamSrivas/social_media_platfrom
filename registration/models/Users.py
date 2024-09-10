from app_registration import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.name}, {self.email}>'

