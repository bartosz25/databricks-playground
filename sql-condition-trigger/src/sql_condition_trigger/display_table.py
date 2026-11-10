import argparse
import logging
import sys

from sql_condition_trigger.spark import get_spark

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout,
    force=True,
)


def display_table():
    params = argparse.ArgumentParser()
    params.add_argument('--table', required=True)
    args = params.parse_args()

    logging.info(f'[display_table] Starting the demo for {args.table}')
    get_spark().table(args.table).show(truncate=False)
    logging.info(f'[display_table] Demo has been completed')
