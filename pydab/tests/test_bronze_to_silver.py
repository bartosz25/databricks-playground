from pyspark.sql import SparkSession

from pydabs_demo.bronze_to_silver import to_silver


def test_to_silver_adds_loaded_at_column():
    spark = SparkSession.builder.master('local[1]').getOrCreate()
    bronze_df = spark.createDataFrame([(1, 'Alice', 'FR'), (2, 'Bob', 'PL')], 'customer_id INT, name STRING, country STRING')

    silver_rows = to_silver(bronze_df).collect()

    assert [(row.customer_id, row.name, row.country) for row in silver_rows] == [(1, 'Alice', 'FR'), (2, 'Bob', 'PL')]
    assert all(row.loaded_at is not None for row in silver_rows)
