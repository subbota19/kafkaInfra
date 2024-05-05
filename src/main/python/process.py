import time

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import from_json, col
from pyspark.sql import Window

KAFKA_CONFIG = {
    "kafka.bootstrap.servers": "192.168.49.2:30003",
    "subscribe": 'test',
    "startingOffsets": "earliest"
}

# Initialize SparkSession
spark = (SparkSession
         .builder
         .appName("KafkaStreamProcessing")
         .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0')
         .getOrCreate())

# Read from Kafka as a DataFrame
kafka_df = spark.readStream.format("kafka").options(**KAFKA_CONFIG).load()

schema = StructType([
    StructField("id", IntegerType()),
    StructField("type", StringType()),
    StructField("message", StringType()),
    StructField("datetime", StringType()),
    StructField("process_id", IntegerType())
])
value_df = (kafka_df
            .select(from_json(col("value").cast("string"), schema).alias("value"))
            .selectExpr('value.id',
                        'value.type',
                        'value.message',
                        'value.datetime',
                        'value.process_id')
            )

df = (value_df.writeStream
      # .partitionBy("process_id")
      .format("csv")
      .option("path", "/home/yauheni/CodeBase/BeamStreamProcessing/src/main/python/output")
      .option("checkpointLocation", "checkpoint_dir")
      .outputMode("append")
      .start())

# Start the streaming application to run until the following happens
# 1. Exception in the running program
# 2. Manual Interruption
# time.sleep(20)
# df.stop()
df.awaitTermination()
