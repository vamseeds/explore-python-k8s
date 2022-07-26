from app.exception.InternalServerError import InternalServerError
from app.util.log_util import get_logger

logger = get_logger()


def validate_response(response):
    response_status_code = response.status_code
    logger.info(f'response status code : {response_status_code}')
    if response_status_code >= 400:
        logger.error(f'Received error response from server: {response.content}')
        raise InternalServerError('Error while Retrieving info from Jenkins. Please Contact Support')

