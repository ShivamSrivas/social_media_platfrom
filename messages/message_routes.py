from flask import Blueprint, render_template

message_bp = Blueprint('messages', __name__)


@message_bp.route('/message_page')
def message_page():
    return render_template('message.html')
