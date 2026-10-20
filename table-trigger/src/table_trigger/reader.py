import argparse
import logging
import sys


def read_tables():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
        stream=sys.stdout,
        force=True,
    )

    params = argparse.ArgumentParser(description="Table update trigger consumer")
    params.add_argument("--scenario", required=True)
    params.add_argument("--trigger_time", required=True)
    params.add_argument("--updated_tables", required=True)
    args = params.parse_args()

    logger.info(f'[{args.scenario}] Started at {args.trigger_time} Reading {args.updated_tables}')
