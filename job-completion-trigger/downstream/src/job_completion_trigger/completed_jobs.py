import argparse
import json
import logging
import sys

from job_completion_trigger.spark import get_spark

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout,
    force=True,
)


def show_completed_jobs():
    params = argparse.ArgumentParser()
    params.add_argument('--completed_jobs', required=True)
    args = params.parse_args()

    logger.info(f'Starting the demo, completed_jobs={args.completed_jobs}')
    completed_jobs = json.loads(args.completed_jobs)
    if completed_jobs:
        get_spark().createDataFrame(completed_jobs).show(truncate=False)
    logger.info('Demo has been completed')
