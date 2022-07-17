from ..util.k8s_util import get_k8s_namespaces, get_k8s_deployments


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
    deployments = get_k8s_deployments(namespace)
    items = deployments.items
    deployment_list = []
    for item in items:
        status = determine_deployment_status(item.status)
        deployment_list.append({'name': item.metadata.name, 'status': status})
    return deployment_list
