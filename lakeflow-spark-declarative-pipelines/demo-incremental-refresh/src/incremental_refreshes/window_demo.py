from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F, Window


@pipelines.materialized_view()
def numbers_window_demo() -> DataFrame:
    number_window = Window.partitionBy("number").orderBy("word")
    return (
        spark.read.table("numbers").withColumns({
            "previous_word": F.lag("word", 1).over(number_window),
            "next_word": F.lead("word", 1).over(number_window)
        })
    )
