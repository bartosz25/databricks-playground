from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.materialized_view()
def numbers_generic_aggregate_demo() -> DataFrame:
    return (
        spark.read.table("numbers").groupBy("number").agg(
            F.count_distinct("word").alias("count_unique_words")
        )
    )
