from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RepartitionCoalesceExample").getOrCreate()

data = [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E")]
df = spark.createDataFrame(data, ["id", "category"])

df_repartitioned = df.repartition(5)
print(f"Number of partitions after repartition: {df_repartitioned.rdd.getNumPartitions()}")

df_coalesced = df_repartitioned.coalesce(2)
print(f"Number of partitions after coalesce: {df_coalesced.rdd.getNumPartitions()}")

df_coalesced.show()

input("Press Enter to stop SparkSession...")
