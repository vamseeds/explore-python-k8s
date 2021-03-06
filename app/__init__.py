from flask import Flask

from .jenkins.routes import jenkins
from .project.routes import project
from .error_handling.error_routes import error_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(project)
    app.register_blueprint(jenkins)
    app.register_blueprint(error_bp)
    return app
