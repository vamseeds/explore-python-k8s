import base64
import configparser
import os
import requests

from app.exception.InternalServerError import InternalServerError
from app.util.log_util import get_logger
from requests.auth import HTTPBasicAuth

from app.util.validation_util import validate_response

logger = get_logger()

config = configparser.ConfigParser()
dir_name = os.path.dirname(__file__)
config_ini = os.path.join(dir_name, '../../resources/config.ini')
config.read(config_ini)
jenkins_base_url = config['jenkins']['url']
jobs_path = config['jenkins']['jobs_path']


def get_basic_auth_header():
    # credentials = bytes(config['jenkins']['user'] + ":" + config['jenkins']['password'], 'utf-8')
    # encoded_credentials = base64.b64encode(credentials).decode()
    # return {"Authorization": "Basic " + encoded_credentials}
    jenkins_user = config['jenkins']['user']
    jenkins_password = config['jenkins']['password']
    return HTTPBasicAuth(jenkins_user, jenkins_password)


def get_jenkins_jobs():
    try:
        path = jenkins_base_url + jobs_path
        logger.info(f'In  jenkins_util.get_jenkins_jobs, Trying to fetch response from {path}')
        response = requests.get(path, auth=get_basic_auth_header())
        validate_response(response)
        response_json = response.json()
        logger.debug(response_json)
        return response_json
    except Exception as api_exception:
        logger.exception(api_exception, extra={'stack': True})
        raise InternalServerError('Error while Retrieving info from Jenkins. Please Contact Support')
