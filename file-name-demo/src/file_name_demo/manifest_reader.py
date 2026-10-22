import argparse
import logging
from file_name_demo.spark import get_spark


def read_manifest():
    logging.basicConfig(level=logging.INFO, format='%(message)s', force=True)
    params = argparse.ArgumentParser()
    params.add_argument('--volume_path', required=True)
    params.add_argument('--checkpoint_path', required=True)
    args = params.parse_args()

    spark = get_spark()
    logging.info(f'[manifest_reader] Reading manifests from {args.volume_path}')
    df = (spark.readStream
          .format('cloudFiles')
          .option('cloudFiles.format', 'text')
          .option('cloudFiles.schemaLocation', f'{args.checkpoint_path}/schema')
          .load(args.volume_path))

    (df.writeStream
     .format('memory')
     .queryName('processed_files')
     .trigger(availableNow=True)
     .option('checkpointLocation', args.checkpoint_path)
     .start().awaitTermination())

    spark.table('processed_files').show(truncate=False)

