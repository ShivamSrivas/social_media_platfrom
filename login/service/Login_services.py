from registration.models.Users import Users
from utlis import logger
from flask import session


class LoginServices:
    logger('logs/login.log', 'LoginServices initiated ', 'INFO')

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_details(self):
        logger('logs/login.log', 'get_details method called', 'INFO')
        try:
            user = Users.query.filter_by(email=self.email).first()
            if user:
                if user.password == self.password:
                    session['user_id'] = user.id
                    session['user_name'] = user.name
                    session['user_email'] = user.email
                    logger('logs/login.log', 'User found', 'INFO')
                    return {"status": True, "messages": "User found", "user": user}
                else:
                    logger('logs/login.log', 'Incorrect password', 'WARNING')
                    return {"status": False, "messages": "Incorrect password"}
            else:
                logger('logs/login.log', 'User not found', 'ERROR')
                return {"status": False, "messages": "User not found"}
        except Exception as e:
            logger('logs/login.log', str(e), 'ERROR')
            return {"status": False, "messages": str(e)}
