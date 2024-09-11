from flask import Blueprint, render_template, request, Response, session, redirect, url_for
from home.service.Home_services import HomeServices
from home.model.Post import Post

home_bp = Blueprint('home', __name__)


@home_bp.route("/home_page")
def home_page():
    try:
        user_name = session.get('user_name')
        post_content = Post.query.all()
        return render_template('home.html', user_name=user_name, post_content=post_content)
    except Exception as error:
        return Response(f"there's an error saying str{error}", status=500)


@home_bp.route('/post', methods=['Post'])
def post():
    try:
        response = None
        if request.method == 'POST':
            post_content = request.form.get('post_content')
            home_services = HomeServices(post_content)
            response = home_services.add_post()
            if response['status']:
                return redirect(url_for('home.home_page'))
        return Response(f"post_content ends with an error {response['messages']}", status=500)
    except Exception as error:
        return Response(f"Error occurred: {error}", status=500)


@home_bp.route("/ai_update")
def ai_updates():
    try:
        return render_template('ai_update.html')
    except Exception as error:
        return Response(f"there's an error saying str{error}", status=500)


@home_bp.route("/climate_change_news")
def climate_change_news():
    try:
        return render_template('climate_change_news.html')
    except Exception as error:
        return Response(f"there's an error saying str{error}", status=500)


@home_bp.route("/tech_news")
def tech_news():
    try:
        return render_template('tech_news.html')
    except Exception as error:
        return Response(f"there's an error saying str{error}", status=500)
