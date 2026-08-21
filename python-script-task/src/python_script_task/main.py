import argparse
import logging

from pyspark.sql import SparkSession

from python_script_task.spark import get_spark


def process_country(country: str, spark: SparkSession):
    spark.createDataFrame([country], 'country STRING').show(truncate=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--country", required=True)
    args = parser.parse_args()
    logging.info(f'Processing {args.country}')

    process_country(
        country=args.country, spark=get_spark()
    )