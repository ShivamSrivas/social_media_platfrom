from flask import Blueprint, render_template, request,Response,session
from home.service.Home_services import HomeServices
from home.model.Post import Post
home_bp = Blueprint('home', __name__)


@home_bp.route("/home_page")
def home_page():
    user_name = session.get('user_name')
    post_content = Post.query.all()
    return render_template('home.html',user_name=user_name,post_content=post_content)


@home_bp.route('/post',methods=['Post'])
def post():
    try:
        if request.method == 'POST':
            post_content = request.form.get('post_content')
            home_services = HomeServices(post_content)
            response=home_services.add_post()
            return Response(f"post_content is : {response}", status=200)
    except Exception as error:
        return Response(f"Error occurred: {error}", status=500)


