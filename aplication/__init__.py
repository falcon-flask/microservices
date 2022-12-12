import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    environment_configuaration = os.getenv('ENVIRONMENT_CONFIGUARATION')
    app.config.from_object(environment_configuaration)

    db.init_app(app)

    with app.app_context():
        # Register blueprints
        return app
    