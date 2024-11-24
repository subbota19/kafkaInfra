from pyspark.sql import SparkSession, functions as sf
from pyspark import StorageLevel

OUTPUT_PATH = "/home/yauheni/main/codeDomain/beamStreamProcessing/data"

spark = SparkSession.builder \
    .appName("Michigan Dataset Processing") \
    .config("spark.executor.memory", "2048m") \
    .config("spark.driver.memory", "2048m") \
    .config("spark.memory.offHeap.enabled", "true") \
    .config("spark.memory.offHeap.size", "2048m") \
    .getOrCreate()

df_review = (spark.
             read.
             json("/home/yauheni/Downloads/ReviewMichigan/review-Michigan-small.json"))

schema = df_review.dtypes

filtered_df = (df_review.filter(df_review.time.isNotNull())
               .withColumn("timestamp", sf.from_unixtime(df_review.time / 1000)))

final_df = (filtered_df
            .withColumn("year", sf.year("timestamp"))
            .withColumn("month", sf.month("timestamp"))
            .withColumn("day", sf.dayofmonth("timestamp")))

final_df.persist(StorageLevel.MEMORY_AND_DISK)

final_df.write.partitionBy("year", "month", "day", "user_id") \
    .mode("overwrite") \
    .parquet(OUTPUT_PATH)


def count_unique_values(df):
    unique_counts = {}

    for column in df.columns:
        print(column)
        unique_count = df.select(column).distinct().count()
        unique_counts[column] = unique_count

    return unique_counts


print(f"schema: {schema}")
# print(f"count_unique_values: {count_unique_values(df=df_review)}")
