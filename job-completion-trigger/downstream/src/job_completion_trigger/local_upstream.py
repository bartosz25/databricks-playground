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


def run_local_upstream():
    params = argparse.ArgumentParser()
    params.add_argument('--should_fail', required=True)
    args = params.parse_args()

    logger.info(f'[s1_local_upstream] Starting the upstream job, should_fail={args.should_fail}')
    if args.should_fail == 'true':
        raise RuntimeError('[s1_local_upstream] Failing the upstream job on demand')
    logger.info('[s1_local_upstream] Upstream job has completed successfully')
