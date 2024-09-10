from registration.models.Users import Users
from flask import session


class LoginServices:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_details(self):
        try:
            user = Users.query.filter_by(email=self.email).first()
            if user:
                if user.password == self.password:
                    # Store user data in session
                    session['user_id'] = user.id
                    session['user_name'] = user.name
                    session['user_email'] = user.email
                    return {"status": True, "messages": "User found", "user": user}
                else:
                    return {"status": False, "messages": "Incorrect password"}
            else:
                return {"status": False, "messages": "User not found"}
        except Exception as e:
            return {"status": False, "messages": str(e)}
