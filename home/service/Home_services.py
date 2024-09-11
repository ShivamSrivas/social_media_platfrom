from home.model.Post import Post
from flask import session
from app_registration import db
import datetime
from utlis import logger


class HomeServices:
    logger('logs/home.log', 'Home initiated', 'INFO')

    def __init__(self, post_content):
        self.post_content = post_content

    def add_post(self):
        logger('logs/home.log', 'add_post method called', 'INFO')
        user_id = session.get('user_id')
        user_name = session.get('user_name')
        if user_id is None:
            return {"status": False, "messages": "User not logged in"}

        current_timestamp = datetime.datetime.now()
        post = Post(user_id=user_id, content=self.post_content, name=user_name, like='', timestamp=current_timestamp)
        try:
            db.session.add(post)
            db.session.commit()
            return {"status": True, "messages": "Post added successfully"}
        except Exception as e:
            db.session.rollback()
            return {"status": False, "messages": f"Error occurred: {e}"}

