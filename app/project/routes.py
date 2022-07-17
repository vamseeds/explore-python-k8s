from flask import Blueprint
from flask import jsonify
from ..service.project_service import get_namespaces, get_deployments
from ..service.validate_service import validate_namespace

project = Blueprint('project', __name__, url_prefix='/projects')


@project.get('/<namespace>')
def get_all_namespaced_deployments(namespace):
    validate_namespace(namespace)
    deployments = get_deployments(namespace)
    return jsonify(deployments), 200


@project.get('')
def get_all_projects():
    namespaces = get_namespaces()
    return jsonify(namespaces), 200
