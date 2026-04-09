from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.table()
def numbers_modulo() -> DataFrame:
    expected_modulo = spark.conf.get("input_parameters.expected_modulo")

    return spark.readStream.table("numbers").filter(f'number % 2 = {expected_modulo}')

