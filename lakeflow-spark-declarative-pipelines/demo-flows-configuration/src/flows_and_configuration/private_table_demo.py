from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.table(private=True)
def numbers_with_processing_time() -> DataFrame:
    return (
        spark.readStream.table("numbers").withColumn("processing_time", F.current_timestamp())
    )

@pipelines.table()
def numbers_decorated_with_processing_time_1() -> DataFrame:
    return spark.readStream.table("numbers_with_processing_time")

@pipelines.table()
def numbers_decorated_with_processing_time_2() -> DataFrame:
    return spark.readStream.table("numbers_with_processing_time")
