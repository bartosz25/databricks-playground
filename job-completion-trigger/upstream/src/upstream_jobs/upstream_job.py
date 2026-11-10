import argparse
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout,
    force=True,
)


def run_upstream_job():
    params = argparse.ArgumentParser()
    params.add_argument('--should_fail', required=True)
    args = params.parse_args()

    logger.info(f'[upstream] Starting the upstream job, should_fail={args.should_fail}')
    if args.should_fail == 'true':
        raise RuntimeError('[upstream] Failing the upstream job on demand')
    logger.info('[upstream] Upstream job has completed successfully')
