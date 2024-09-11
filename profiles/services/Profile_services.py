from app_registration import db
from registration.models.Users import Users
from home.model.Post import Post
from utlis import  logger


class ProfileServices:
    logger('logs/profile.log', 'ProfileServices  initiated', 'INFO')

    def __init__(self, user_id, new_password=None):
        self.user_id = user_id
        self.new_password = new_password

    def password_update(self):
        logger('logs/profile.log', 'password_update  method called', 'INFO')
        user = Users.query.get(self.user_id)
        if user:
            user.password = self.new_password
            try:
                db.session.commit()
                return {"status": True, "message": "Password updated successfully"}
            except Exception as e:
                db.session.rollback()
                logger('logs/profile.log', f' there"s an error in password_update saying {e}', 'ERROR')
                return {"status": False, "message": f"Error occurred: {e}"}
        else:
            logger('logs/profile.log', 'ProfileServices  User not found', 'WARNING')
            return {"status": False, "message": "User not found"}

    def delete_post(self, timestamp):
        logger('logs/profile.log', 'delete_post  method called', 'INFO')
        post = Post.query.filter_by(user_id=self.user_id, timestamp=timestamp).first()
        if post:
            try:
                db.session.delete(post)
                db.session.commit()
                return {"status": True, "message": "Post deleted successfully"}
            except Exception as e:
                db.session.rollback()
                logger('logs/profile.log', f'there"s an error in delete_post  saying {e}', 'ERROR')
                return {"status": False, "message": f"Error occurred: {e}"}
        else:
            logger('logs/profile.log', f'there"s an error in delete_post  saying Post not found', 'ERROR')
            return {"status": False, "message": "Post not found"}
