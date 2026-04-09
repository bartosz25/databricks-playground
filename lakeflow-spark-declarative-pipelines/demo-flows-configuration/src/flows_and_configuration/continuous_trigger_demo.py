from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.table()
def numbers_for_continuous_trigger_demo() -> DataFrame:
    return spark.readStream.table("numbers")

