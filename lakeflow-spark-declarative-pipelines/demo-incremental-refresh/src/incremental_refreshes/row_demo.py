from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.materialized_view()
def numbers_output_for_row_demo() -> DataFrame:
    return (
        spark.read.table("raw_numbers_partitioned")
    )
