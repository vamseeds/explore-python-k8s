from .validate_service import validate_duplicate_namespace, validate_namespace, validate_create_namespace_request
from ..util.k8s_util import get_k8s_namespaces, get_k8s_deployments, create_k8s_namespace


def get_namespaces():
    namespaces_k8s_json = get_k8s_namespaces()
    items = namespaces_k8s_json.items
    ns_list = []
    for item in items:
        ns_list.append(item.metadata.name)
    return ns_list


def determine_deployment_status(deployment_status):
    conditions = deployment_status.conditions
    for condition in conditions:
        if condition.reason == 'MinimumReplicasAvailable' and condition.status == 'True':
            return "UP"
    return "DOWN"


def get_deployments(namespace):
    validate_namespace(namespace, get_namespaces())
    deployments = get_k8s_deployments(namespace)
    items = deployments.items
    deployment_list = []
    for item in items:
        status = determine_deployment_status(item.status)
        deployment_list.append({'name': item.metadata.name, 'status': status})
    return deployment_list


def create_namespace(request_json):
    validate_create_namespace_request(request_json)
    validate_duplicate_namespace(request_json['name'], get_namespaces())
    create_k8s_namespace(request_json['name'])
