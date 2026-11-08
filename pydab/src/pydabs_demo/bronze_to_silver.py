import argparse
import logging
import sys

from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

from pydabs_demo.spark import get_spark

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    stream=sys.stdout,
    force=True,
)


def to_silver(bronze_df: DataFrame) -> DataFrame:
    return bronze_df.withColumn('loaded_at', current_timestamp())


def bronze_to_silver():
    params = argparse.ArgumentParser()
    params.add_argument('--bronze_table', required=True)
    params.add_argument('--silver_table', required=True)
    args = params.parse_args()

    logging.info(f'[bronze_to_silver] Starting the demo for {args.bronze_table} -> {args.silver_table}')
    get_spark().table(args.bronze_table).show(truncate=False)
    logging.info(f'[bronze_to_silver] Demo has been done')
