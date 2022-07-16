from flask import Flask
from .project.routes import project


def create_app():
    app = Flask(__name__)

    app.register_blueprint(project)
    return app
