from ..util.jenkins_util import get_jenkins_jobs
from ..util.log_util import get_logger

logger = get_logger()


def get_jobs():
    jobs_response = get_jenkins_jobs()
    jobs = []
    if 'jobs' in jobs_response:
        jobs_json_array = jobs_response['jobs']
        for job in jobs_json_array:
            jobs.append(job['name'])
    else:
        logger.error('Something Fishy!jobs node not found in jenkins response....')
    return jobs
