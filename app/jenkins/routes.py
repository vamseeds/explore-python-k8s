from flask import Blueprint, request
from flask import jsonify
from ..service.jenkins_service import get_jobs
from ..util.log_util import get_logger
from flask_negotiate import consumes
from flask_cors import CORS

jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')

CORS(jenkins)

logger = get_logger()


@jenkins.get('/jobs')
def get_all_jobs():
    jobs = get_jobs()
    return jsonify(jobs), 200
