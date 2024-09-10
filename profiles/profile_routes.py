from flask import Blueprint, render_template, redirect, request, session
from home.model.Post import Post
from profiles.services.Profile_services import ProfileServices

profile_bp = Blueprint('profiles', __name__)


@profile_bp.route('/profile_page')
def profile_page():
    data = {
        'user_name': session.get('user_name'),
        'user_id': session.get('user_id'),
        'email': session.get('user_email'),
        'post_content': Post.query.filter_by(user_id=session.get('user_id')).all()
    }
    return render_template('profile.html', data=data)


@profile_bp.route('/password_update', methods=['POST'])
def password_update():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password == confirm_password:
            user_id = session.get('user_id')
            if user_id:
                profile_service = ProfileServices(user_id, new_password)
                result = profile_service.password_update()
                if result['status']:
                    return redirect('/profiles/profile_page')
                else:
                    return render_template('profile.html', data={'error': result['message']})
            else:
                return render_template('profile.html', data={'error': "User not logged in"})
        else:
            return render_template('profile.html', data={'error': "Passwords do not match"})


@profile_bp.route('/delete_post', methods=['POST'])
def delete_post():
    user_id = session.get('user_id')
    timestamp = request.form.get('timestamp')

    if user_id and timestamp:
        profile_service = ProfileServices(user_id)
        response = profile_service.delete_post(timestamp)
        if response['status']:
            return redirect('/profiles/profile_page')
        else:
            return render_template('profile.html', data={'error': response['message']})
    else:
        return render_template('profile.html', data={'error': "User not logged in or timestamp missing"})
