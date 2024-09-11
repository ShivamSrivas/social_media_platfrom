from flask import session
from app_registration import db
from messages.model.Messages import Messages
from utlis import logger


class MessageServices():
    logger('logs/message.log', 'MessageServices  initiated', 'INFO')

    def __init__(self):
        self.user_id = session.get('user_id')
        self.user_name = session.get('user_name')
        self.user_email = session.get('user_email')

    def add_messages(self, messages):
        logger('logs/message.log', 'add_messages  method called', 'INFO')
        try:
            add_msg = Messages(user_id=self.user_id, name=self.user_name, email=self.user_email, message=messages)
            db.session.add(add_msg)
            db.session.commit()
            db.session.close()
            return {
                'status': True,
                'message': 'Message added successfully'
            }
        except Exception as error:
            print(error, "error")
            return {
                'status': False,
                'message': 'Message not added'
            }

    def get_all_message(self):
        logger('logs/message.log', 'get_all_message  method called', 'INFO')
        try:
            get_all_msg = Messages.query.all()
            return {"status": True, "data": get_all_msg}
        except Exception as error:
            return {"status": False, "error": error}
