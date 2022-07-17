from app.exception.NotFoundException import NotFoundException
from .project_service import get_namespaces


def validate_namespace(namespace):
    namespaces = get_namespaces()
    if namespace not in namespaces:
        raise NotFoundException('Namespace not found', 404)
