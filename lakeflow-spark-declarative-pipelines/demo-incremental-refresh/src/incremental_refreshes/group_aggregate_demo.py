from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.materialized_view()
def numbers_group_aggregate_demo() -> DataFrame:
    return (
        spark.read.table("numbers").groupBy("number").agg(
            F.count(F.col("word")).alias("word_count"),
            F.min(F.col("word")).alias("min_word"),
            F.max(F.col("word")).alias("max_word")
        )
    )
