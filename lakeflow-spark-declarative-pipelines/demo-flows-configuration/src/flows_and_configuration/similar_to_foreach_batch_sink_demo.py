from pyspark import pipelines
from pyspark.sql import DataFrame

@pipelines.table()
def numbers_similar_foreach_sink() -> DataFrame:
    return spark.readStream.table("numbers")
