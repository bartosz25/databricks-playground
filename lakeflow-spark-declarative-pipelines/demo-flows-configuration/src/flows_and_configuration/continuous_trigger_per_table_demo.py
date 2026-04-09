from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.table(
    spark_conf={"pipelines.trigger.interval" : "2 minutes"}
)
def numbers_for_per_table_continuous_trigger_demo() -> DataFrame:
    return spark.readStream.table("numbers")


@pipelines.materialized_view(
    spark_conf={"pipelines.trigger.interval" : "5 minutes"}
)
def numbers_for_per_table_continuous_trigger_demo_materialized_view():
    return spark.read.table('numbers')