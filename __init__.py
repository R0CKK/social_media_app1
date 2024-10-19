# social_media_app/__init__.py
from flask import Flask
from .shared.utils.db_utils import db  # Adjust import according to your structure
from .shared.models.user_model import User  # Import your models as needed

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object('config.Config')  # Adjust the config path as necessary
    
    # Initialize the database
    db.init_app(app)
    
    with app.app_context():
        # Import routes or views here to register with the app
        from .views import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
