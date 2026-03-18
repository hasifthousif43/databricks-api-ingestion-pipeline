from pyspark.sql.functions import *

df = spark.readStream.format("delta") \
    .load("/mnt/bronze/api_data")

df_clean = df \
    .withWatermark("ingestion_time", "10 minutes") \
    .dropDuplicates(["id"])

query = df_clean.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/silver") \
    .start("/mnt/silver/api_data")
