from app_registration import db
import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), nullable=False)
    content = db.Column(db.String(length=255), nullable=False)
    like = db.Column(db.String(length=255), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, content, user_id, name, like, timestamp):
        self.content = content
        self.user_id = user_id
        self.name = name
        self.like = like
        self.timestamp = timestamp

    def __repr__(self):
        return f'<Post {self.id}, {self.user_id}, {self.name}, {self.like}, {self.content}>'
