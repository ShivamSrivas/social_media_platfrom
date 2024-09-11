from flask import Blueprint, render_template, Response, redirect, url_for, request
from messages.service.Message_services import MessageServices

message_bp = Blueprint('messages', __name__)


@message_bp.route('/message_page')
def message_page():
    try:
        get_msg = MessageServices()
        get_msg = get_msg.get_all_message()
        print(get_msg.get('data'),"print(get_msg)")
        for msg in get_msg.get('data'):
            print(msg.name)
        return render_template('message.html', data=get_msg.get('data'))
    except Exception as error:
        print(error,"----->")
        return Response(status=500)


@message_bp.route('/add_message', methods=['POST'])
def add_message():
    try:
        if request.method == 'POST':
            msg = request.form.get('message')
            msg_services = MessageServices()
            response = msg_services.add_messages(msg)
            if response['status']:
                return redirect(url_for('messages.message_page'))
        return redirect(url_for('message.message_page'))
    except Exception as error:
        return Response(status=500)
