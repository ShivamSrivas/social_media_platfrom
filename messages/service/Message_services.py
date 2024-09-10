from flask import session


class MessageServices():
    def __init__(self):
        self.user_id = session.get('user_id')
        self.user_name = session.get('user_name')
        self.user_email = session.get('user_email')
