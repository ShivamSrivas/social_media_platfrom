from flask import Blueprint, request, Response, render_template
from registration.services.Registration_services import RegistrationService

# Define the blueprint
registration_bp = Blueprint('registration', __name__)


@registration_bp.route('/registration_page')
def registration_page():
    return render_template('registration.html')


# Create a new registration route
@registration_bp.route('/new_registrations', methods=['POST'])
def new_registration():
    try:
        if request.method == "POST":
            name = request.form.get('name')
            age = request.form.get('age')
            email = request.form.get('email')
            password = request.form.get('password')

        # Pass the form data to the RegistrationService
            new_registrations = RegistrationService(name, age, email, password)
            new_registrations.register()

        return Response("Registration successful", status=200)

    except Exception as error:
        return Response(f"Error occurred: {error}", status=500)
