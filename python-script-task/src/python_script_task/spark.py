import logging

from pyspark.sql import SparkSession


def get_spark() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession  # type: ignore[reportMissingImports]

        return DatabricksSession.builder.getOrCreate()
    except ImportError:
        logging.info("Databricks is not installed, using local SparkSession.")
        return SparkSession.builder.getOrCreate()