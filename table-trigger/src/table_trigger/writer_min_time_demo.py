import logging
import sys
import time
from datetime import datetime

from table_trigger.spark import get_spark


def write_data():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
        force=True,
    )

    output_table = 'workspace.table_trigger_demo.min_time_between_triggers_seconds_src'
    logger.info(f'Started writing data to {output_table}')


    for run in range(0, 4):
        logger.info(f'The writing round number {run}')
        get_spark().sql(f'INSERT INTO {output_table} (id) VALUES (200{run})')
        insert_time = datetime.now().strftime("%d %B %Y %H:%M:%S")
        logger.info(f'Finished writing to {output_table} at {insert_time}')
        time.sleep(30)
        wakeup_time = datetime.now().strftime("%d %B %Y %H:%M:%S")
        logger.info(f'Woke up at {wakeup_time}')

    logger.info(f'Completed writing data to {output_table}')
