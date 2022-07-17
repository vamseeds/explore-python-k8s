import kubernetes.client.exceptions
from kubernetes import config, client
from .log_util import get_logger
from app.exception.InternalServerError import InternalServerError

logger = get_logger()


def get_k8s_namespaces():
    try:
        config.load_kube_config()
    except Exception as exception:
        logger.info('Unable to load kube config... Trying to load incluster config')
        config.load_incluster_config()
    core_api_client = client.CoreV1Api()
    try:
        response = core_api_client.list_namespace()
        logger.debug(response)
        return response
    except kubernetes.client.exceptions.ApiException as api_exception:
        logger.exception(api_exception, extra={'stack': True})
        raise InternalServerError('Error while Retrieving namespaces from cluster', 500)


def get_k8s_deployments(namespace):
    try:
        config.load_kube_config()
    except Exception as exception:
        logger.info('Unable to load kube config... Trying to load incluster config')
        config.load_incluster_config()
    apps_api_client = client.AppsV1Api()
    try:
        response = apps_api_client.list_namespaced_deployment(namespace=namespace)
        logger.debug(response)
        return response
    except kubernetes.client.exceptions.ApiException as api_exception:
        logger.exception(api_exception, extra={'stack': True})
        raise InternalServerError('Error while Retrieving deployments from cluster', 500)
