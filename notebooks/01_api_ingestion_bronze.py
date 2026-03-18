from pyspark.sql.functions import current_timestamp
import json

# Load config
config = json.loads(dbutils.fs.head("/FileStore/configs/api_config.json"))

from src.api_client import fetch_api_data

data = fetch_api_data(config["api_url"])

df = spark.createDataFrame(data)

df = df.withColumn("ingestion_time", current_timestamp())

df.write.format("delta") \
    .mode("append") \
    .save("/mnt/bronze/api_data")
