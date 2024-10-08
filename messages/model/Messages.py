from app_registration import db
import  datetime


class Messages(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    name = db.Column(db.String(255),nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow,nullable=False)
    message = db.Column(db.String(255),nullable=False)

    def __init__(self,user_id,name,email,message):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f'<{self.id},{self.user_id},{self.name},{self.email},{self.timestamp},{self.message}>'
