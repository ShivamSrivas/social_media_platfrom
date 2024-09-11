from flask import Blueprint, render_template, Response, redirect, url_for, request
from messages.service.Message_services import MessageServices

message_bp = Blueprint('messages', __name__)


@message_bp.route('/message_page')
def message_page():
    try:
        response = None
        get_msg = MessageServices()
        response = get_msg.get_all_message()
        if response['status']:
            return render_template('message.html', data=response.get('data'))
        return Response(f"There's an error {response['data']} ", status=500)
    except Exception as error:
        return Response(f"There's an error {error} ",status=500)


@message_bp.route('/add_message', methods=['POST'])
def add_message():
    try:
        response = None
        if request.method == 'POST':
            msg = request.form.get('message')
            msg_services = MessageServices()
            response = msg_services.add_messages(msg)
            if response['status']:
                return redirect(url_for('messages.message_page'))
        return Response(f"There's an error {response['message']} ",status=500)
    except Exception as error:
        return Response(f"There's an error {error} ",status=500)
