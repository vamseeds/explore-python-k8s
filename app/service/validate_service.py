from app.exception.NotFoundException import NotFoundException
from ..exception.BadRequestException import BadRequestException
from ..exception.DuplicateException import DuplicateException


def validate_namespace(namespace, namespaces):
    if namespace not in namespaces:
        raise NotFoundException('Namespace not found')


def validate_duplicate_namespace(namespace, namespaces):
    if namespace in namespaces:
        raise DuplicateException(f'Project already exists with name {namespace}')


def validate_create_namespace_request(request_json):
    if 'name' not in request_json:
        raise BadRequestException('name is mandatory in request body')
