from flask import session
from app_registration import db
from messages.model.Messages import Messages
import datetime





class MessageServices():
    def __init__(self):
        self.user_id = session.get('user_id')
        self.user_name = session.get('user_name')
        self.user_email = session.get('user_email')

    def add_messages(self, messages):
        try:
            add_msg = Messages(user_id=self.user_id, name=self.user_name, email=self.user_email, message=messages)
            db.session.add(add_msg)
            db.session.commit()
            db.session.close()
            return {
                'status': True,
                'msg': 'Message added successfully'
            }
        except Exception as error:
            print(error, "error")
            return {
                'status': False,
                'msg': 'Message not added'
            }
    def get_all_message(self):
        try:
            get_all_msg = Messages.query.all()
            return {"status": True, "data": get_all_msg}
        except Exception as error:
            return {"status": False, "error": error}