from flask import Blueprint
from flask import jsonify
from ..util.k8s_util import get_namespaces

project = Blueprint('project', __name__, url_prefix='/projects')


@project.get('')
def get_all_projects():
    namespaces = get_namespaces()
    return jsonify(namespaces), 200
