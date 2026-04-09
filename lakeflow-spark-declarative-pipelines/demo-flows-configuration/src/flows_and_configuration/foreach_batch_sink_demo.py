from pyspark import pipelines
from pyspark.sql import DataFrame, functions as F


@pipelines.foreach_batch_sink(name="foreach_batch_sink_example")
def foreach_batch_sink_example(df: DataFrame, batch_id: int):
    df.persist()
    print(f'------ DataFrame content for {batch_id} ---------')
    df.show(truncate=False)
    mode = 'append'
    if batch_id == 0:
        mode = 'overwrite'
    df.write.format('delta').mode(mode).saveAsTable('workspace.default.numbers_foreach_sink')
    print(f'------ DataFrame count for {batch_id}   ---------')
    print(f'All rows in the DataFrame={df.count()}')
    df.unpersist()

@pipelines.append_flow(
    target="foreach_batch_sink_example",
)
def printer_and_counter_flow():
  return spark.readStream.table("numbers")
