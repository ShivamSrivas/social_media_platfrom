from app_registration import db
from registration.models.Users import Users
from utlis import  logger

class RegistrationService:
    logger('logs/registration.log', 'RegistrationService  initiated', 'INFO')
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def register(self):
        logger('logs/registration.log', 'register  method called', 'INFO')
        try:
            users = Users(
                name=self.name,
                age=self.age,
                email=self.email,
                password=self.password
            )
            db.session.add(users)
            db.session.commit()
            logger('logs/registration.log', 'Users Successfully registered', 'INFO')
            return {"status":True,"message": 'Successfully registered'}
        except Exception as e:
            db.session.rollback()
            logger('logs/registration.log', f"An error occurred: {e}", 'INFO')
            return {'status':False,"message": f"An error occurred: {e}"}
        finally:
            db.session.close()