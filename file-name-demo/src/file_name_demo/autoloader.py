import argparse
import logging
from pyspark.sql.functions import col
from file_name_demo.spark import get_spark


def read_files():
    logging.basicConfig(level=logging.INFO, format='%(message)s', force=True)
    params = argparse.ArgumentParser()
    params.add_argument('--volume_path', required=True)
    params.add_argument('--checkpoint_path', required=True)
    args = params.parse_args()

    spark = get_spark()
    volume_path = args.volume_path
    checkpoint_path = args.checkpoint_path

    logging.info(f'[autoloader] Reading from {volume_path}')
    df = (spark.readStream
          .format('cloudFiles')
          .option('cloudFiles.format', 'csv')
          .option('header', 'true')
          .option('cloudFiles.schemaLocation', f'{checkpoint_path}/schema')
          .load(volume_path)
          .select('id', 'amount', col('_metadata.file_path').alias('file_path')))

    (df.writeStream
     .format('memory')
     .queryName('processed_files')
     .trigger(availableNow=True)
     .option('checkpointLocation', checkpoint_path)
     .start().awaitTermination())

    spark.table('processed_files').show(truncate=False)
