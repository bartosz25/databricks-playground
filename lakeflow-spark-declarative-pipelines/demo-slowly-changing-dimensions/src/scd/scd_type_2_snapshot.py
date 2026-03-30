from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.view
def blog_posts():
  return spark.read.table("workspace.default.blog_posts_raw")

dp.create_streaming_table("blog_posts_scd_type_2_snapshot")

dp.create_auto_cdc_from_snapshot_flow(
  target = "blog_posts_scd_type_2_snapshot",
  source = "blog_posts",
  keys = ["id"],
  stored_as_scd_type = 2
)
