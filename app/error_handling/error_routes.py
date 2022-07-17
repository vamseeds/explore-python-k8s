from flask import Blueprint, jsonify

from app.exception.BadRequestException import BadRequestException
from app.exception.DuplicateException import DuplicateException
from app.exception.InternalServerError import InternalServerError
from app.exception.NotFoundException import NotFoundException
from ..util.log_util import get_logger

error_bp = Blueprint('error', __name__)
logger = get_logger()


@error_bp.app_errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not Found'}), 404


@error_bp.app_errorhandler(InternalServerError)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), error.error_code


@error_bp.app_errorhandler(NotFoundException)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), error.error_code


@error_bp.app_errorhandler(DuplicateException)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), error.error_code


@error_bp.app_errorhandler(BadRequestException)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), error.error_code



