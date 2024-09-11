from flask import Blueprint, request, Response, render_template, redirect, url_for
from registration.services.Registration_services import RegistrationService

registration_bp = Blueprint('registration', __name__)


@registration_bp.route('/registration_page')
def registration_page():
    return render_template('registration.html')


@registration_bp.route('/new_registrations', methods=['POST'])
def new_registration():
    try:
        response = None
        if request.method == "POST":
            name = request.form.get('name')
            age = request.form.get('age')
            email = request.form.get('email')
            password = request.form.get('password')
            new_registrations = RegistrationService(name, age, email, password)
            response = new_registrations.register()
            if response['status']:
                return redirect(url_for("login.login_page"))
            return Response(f"Registration unsuccessful {response['message']}", status=500)
        return Response("Registration was not done", status=500)
    except Exception as error:
        return Response(f"Error occurred: {error}", status=500)
