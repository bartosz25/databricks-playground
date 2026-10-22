import argparse
import logging

from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from file_name_demo.spark import get_spark


def generate_manifest():
    logging.basicConfig(level=logging.INFO, format='%(message)s', force=True)
    params = argparse.ArgumentParser()
    params.add_argument('--volume_path', required=True)
    params.add_argument('--checkpoint_path', required=True)
    params.add_argument('--manifest_path', required=True)
    args = params.parse_args()

    spark = get_spark()
    logging.info(f'[manifest_generator] Reading from {args.volume_path}')
    df = (spark.readStream
          .format('cloudFiles')
          .option('cloudFiles.format', 'csv')
          .option('header', 'true')
          .option('cloudFiles.schemaLocation', args.checkpoint_path + '/schema')
          .load(args.volume_path))

    def write_manifest(batch_df: DataFrame, _):
        (batch_df.select(col('_metadata.file_path').alias('file_path')).distinct().coalesce(1)
         .write.format('text').mode('overwrite').save(args.manifest_path))

    query = (df.writeStream
             .foreachBatch(write_manifest)
             .trigger(availableNow=True)
             .option('checkpointLocation', args.checkpoint_path)
             .start())
