from flask import Blueprint, render_template

notifications_bp = Blueprint('notifications', __name__)


@notifications_bp.route('/notifications_page')
def notifications_page():
    return render_template('notification.html')
