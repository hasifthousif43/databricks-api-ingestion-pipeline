from pyspark.sql.functions import *

df = spark.readStream.format("delta") \
    .load("/mnt/silver/api_data")

agg_df = df.groupBy(
    window(col("ingestion_time"), "5 minutes"),
    col("userId")
).count()

agg_df.writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "/mnt/checkpoints/gold") \
    .start("/mnt/gold/api_summary")
