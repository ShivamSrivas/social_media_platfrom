from app_registration import db
from registration.models.Users import Users


class RegistrationService:
    def __init__(self, name, age, email, password):
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def register(self):
        try:
            # Create a new Registration instance
            users = Users(
                name=self.name,
                age=self.age,
                email=self.email,
                password=self.password
            )
            db.session.add(users)
            db.session.commit()
            return {"msg": 'Successfully registered'}
        except Exception as e:
            # Rollback in case of an error
            db.session.rollback()
            print(f"An error occurred: {e}")
            return {"msg": f"An error occurred: {e}"}
        finally:
            # Ensure that the session is always closed
            db.session.close()