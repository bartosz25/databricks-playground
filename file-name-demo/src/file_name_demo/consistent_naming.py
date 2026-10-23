import argparse
import logging
import os
from datetime import datetime
from pyspark.sql import functions as F
from file_name_demo.spark import get_spark


def read_files():
    logging.basicConfig(level=logging.INFO, format='%(message)s', force=True)
    params = argparse.ArgumentParser()
    params.add_argument('--volume_path', required=True)
    params.add_argument('--trigger_date', required=True)
    args = params.parse_args()

    spark = get_spark()
    date_suffix = datetime.strptime(args.trigger_date, '%Y-%m-%d').strftime('%Y%m%d')

    logging.info(f'[consistent_naming] Reading files for {date_suffix} from {args.volume_path}')
    pairs = ['USD_EUR', 'EUR_GBP']
    conversion_rates = (spark.read.schema('from_currency STRING, to_currency STRING, rate DOUBLE').csv(
        path=[os.path.join(args.volume_path, f'{pair}_{date_suffix}.csv') for pair in pairs], header=True
    )).withColumn('source_file', F.col('_metadata.file_path'))

    conversion_rates.show(truncate=False)
