from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F

@pipelines.materialized_view()
def broken_append_only() -> DataFrame:
    return (
        spark.read.table("numbers")
        .withColumn("random_value", F.rand())
    )
