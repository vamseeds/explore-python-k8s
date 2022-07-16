from kubernetes import config, client


def get_namespaces():
    try:
        config.load_kube_config()
    except:
        config.load_incluster_config()
    core_api_client = client.CoreV1Api()
    response = core_api_client.list_namespace()
    print(response)
    items = response.items
    ns_list = []
    for item in items:
        ns_list.append(item.metadata.name)
    return ns_list
