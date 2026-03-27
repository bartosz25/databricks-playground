from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.view
def blog_posts():
  return spark.readStream.table("workspace.default.blog_posts_raw")

dp.create_streaming_table("blog_posts_scd_type_1")

dp.create_auto_cdc_flow(
  target = "blog_posts_scd_type_1",
  source = "blog_posts",
  keys = ["id"],
  sequence_by = F.col("date_changed"),
  apply_as_deletes = F.expr("operation = 'DELETE'"),
  apply_as_truncates = F.expr("operation = 'TRUNCATE'"),
  except_column_list = ["operation", "date_changed"], # we don't want to store these 2 columns
  stored_as_scd_type = 1
)