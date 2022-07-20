from flask import Blueprint, request
from flask import jsonify
from ..service.project_service import get_namespaces, get_deployments, create_namespace
from ..util.log_util import get_logger
from flask_negotiate import consumes
from flask_cors import CORS

project = Blueprint('project', __name__, url_prefix='/projects')

CORS(project)

logger = get_logger()


@project.get('/<namespace>')
def get_all_namespaced_deployments(namespace):
    deployments = get_deployments(namespace)
    return jsonify(deployments), 200


@project.get('')
def get_all_projects():
    namespaces = get_namespaces()
    return jsonify(namespaces), 200


@project.post('')
@consumes('application/json')
def create_project():
    data = request.get_json()
    logger.info('Received a namespace create request : %s', data)
    create_namespace(data)
    return jsonify({'message': f'Project has been successfully created with name {data["name"]}'}), 201
