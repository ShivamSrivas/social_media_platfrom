from flask import Blueprint,request
from flask import render_template,redirect,url_for
from flask import  Response
from login.service.Login_services import LoginServices

login_bp = Blueprint('login', __name__)


@login_bp.route('/')
def login_page():
    return render_template('login.html')


@login_bp.route('/login',methods=['Post'])
def get_details():
    flag = None
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            login_services = LoginServices(email, password)
            flag = login_services.get_details()
            if flag['status']:
                return redirect(url_for("home.home_page"))
        return Response(flag['messages'], status=500)

    except Exception as error:
        return Response(f"Error occurred: {error}", status=500)
