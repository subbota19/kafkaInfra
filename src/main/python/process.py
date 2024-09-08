from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType
from pyspark.sql.functions import from_json, col, to_timestamp, current_timestamp, window

KAFKA_CONFIG = {
    "kafka.bootstrap.servers": "192.168.49.2:30000",
    "subscribe": 'ABC',
    "startingOffsets": "earliest"
}

# local testing
# .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.3')
# .config('spark.jars.packages', 'org.apache.spark:spark-streaming-kafka-0-10_2.13:3.4.3')

# Initialize SparkSession
spark = (SparkSession
         .builder
         .appName("KafkaStreamProcessing")
         .getOrCreate())

# Read from Kafka as a DataFrame
kafka_df = (spark.readStream
            .format("kafka")
            .options(**KAFKA_CONFIG)
            .load())

schema = StructType([
    StructField("id", LongType()),
    StructField("type", StringType()),
    StructField("message", StringType()),
    StructField("datetime", StringType()),
    StructField("process_id", LongType())
])

kafka_df = (kafka_df.
            withColumn('value', from_json(col('value').
                                          cast("STRING"), schema)))

kafka_df = (kafka_df
            .select(
    col('value.id').alias('id'),
    col('value.type').alias('type'),
    col('value.message').alias('message'),
    col('value.datetime').alias('datetime'),
    col('value.process_id').alias('process_id'))
            .withColumn("event_time", to_timestamp(col("datetime")))
            .withColumn("process_time", current_timestamp())

            .withWatermark('event_time', '10 seconds'))

kafka_df = (kafka_df
            .groupBy(
    window(col('event_time'), '1 minute', '1 minute'), col('process_id'))
            .count().alias('NumberOfProcess')
            .orderBy(col('NumberOfProcess')))

df = (kafka_df.writeStream
      # .partitionBy("process_id")
      .format("console")
      # .outputMode("append")
      .outputMode("update")
      .start())

# Start the streaming application to run until the following happens
# 1. Exception in the running program
# 2. Manual Interruption
# time.sleep(20)
# df.stop()
df.awaitTermination()
