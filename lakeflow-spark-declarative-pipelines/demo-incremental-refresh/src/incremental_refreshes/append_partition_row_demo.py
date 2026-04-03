from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.materialized_view(
    partition_cols=['number']
)
def numbers_partitioned_output_for_append_partition_row_demo() -> DataFrame:
    return (
        spark.read.table("raw_numbers_partitioned")
    )
