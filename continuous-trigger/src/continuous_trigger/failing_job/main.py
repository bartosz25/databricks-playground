from pyspark.sql import DataFrame

from continuous_trigger.arguments import get_parser
from continuous_trigger.producer import write_files_to_tmp
from continuous_trigger.spark_session_factory import create_spark_session_for_localhost_or_databricks


def main():
    parser = get_parser()
    spark = create_spark_session_for_localhost_or_databricks()

    write_files_to_tmp(parser.path)

    reader = spark.readStream.text(path=parser.path)

    def fail_foreach_path(df: DataFrame, batch: int):
        raise RuntimeError('Failing job')

    (reader.writeStream.foreachBatch(fail_foreach_path)
     .option('checkpointLocation', f'/tmp/checkpoint_{parser.path}')
     .trigger(processingTime='30 seconds')
     .start())
