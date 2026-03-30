from pyspark.sql import SparkSession


def create_spark_session_for_localhost_or_databricks() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession
        return DatabricksSession.builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.master('local[*]').getOrCreate()
