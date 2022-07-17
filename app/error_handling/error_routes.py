from flask import Blueprint, jsonify

from app.exception.InternalServerError import InternalServerError
from app.exception.NotFoundException import NotFoundException

error_bp = Blueprint('error', __name__)


@error_bp.app_errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not Found'}), 404


@error_bp.app_errorhandler(InternalServerError)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), 500


@error_bp.app_errorhandler(NotFoundException)
def general_error(error):
    response = {
        "error": error.details,
        "code": error.error_code
    }
    return jsonify(response), 404
