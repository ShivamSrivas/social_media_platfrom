from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import secrets
import logging
from logging.handlers import RotatingFileHandler

# Initialize SQLAlchemy and Migrate instances
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Application factory that configures and returns the Flask app instance.
    """
    # Create Flask application instance
    app = Flask(__name__)

    # Set secret key for session management and CSRF protection
    app.secret_key = secrets.token_hex(16)

    # Configure the app (e.g., database URI, disable track modifications)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost/social_media_platform"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import blueprints within the factory function to avoid circular imports
    from registration.registration_routes import registration_bp
    from login.login_routes import login_bp
    from home.home_routes import home_bp
    from messages.message_routes import message_bp
    from notifications.notification_routes import notifications_bp
    from profiles.profile_routes import profile_bp

    # Initialize database and migration extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints with URL prefixes
    app.register_blueprint(login_bp)
    app.register_blueprint(registration_bp, url_prefix='/registration')
    app.register_blueprint(home_bp, url_prefix='/home')
    app.register_blueprint(message_bp, url_prefix='/messages')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(profile_bp, url_prefix='/profiles')

    # Setup logging
    if not app.debug:
        handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.ERROR)
        app.logger.addHandler(handler)

    return app
