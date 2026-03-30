from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.table()
def raw_numbers() -> DataFrame:
    return (spark.readStream.format("rate").option("rowsPerSecond", 10)
        .option("numPartitions", 2).load())

@pipelines.table()
def decorated_numbers() -> DataFrame:
    return (
        spark.readStream.table("raw_numbers").withColumn("processed_at", F.current_timestamp())
    )

@pipelines.table()
def numbers_1() -> DataFrame:
    return (spark.readStream.table("decorated_numbers"))

@pipelines.table()
def numbers_2() -> DataFrame:
    return (spark.readStream.table("decorated_numbers"))