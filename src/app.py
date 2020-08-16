from flask import Flask
from .config import app_config
from .models import db, bcrypt

def create_app(env_name):
    """
    Create app
    """

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # initializing bcrypt
    bcrypt.init_app(app)

    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """
        Example endpoint
        """
        return "Congratulations! Your endpoint is working now"

    return app