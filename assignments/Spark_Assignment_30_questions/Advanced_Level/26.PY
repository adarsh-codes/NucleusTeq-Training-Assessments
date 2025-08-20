from pyspark.sql import SparkSession
from pyspark.storagelevel import StorageLevel
import time

spark = SparkSession.builder.appName("CachePersistExample").getOrCreate()

data = [(i, i * 2) for i in range(1000000)]
df = spark.createDataFrame(data, ["num", "double_num"])

df.cache()

start_time = time.time()
df.count()
print(f"Time taken after caching: {time.time() - start_time} seconds")

df.persist(StorageLevel.MEMORY_AND_DISK)

start_time = time.time()
df.count()
print(f"Time taken after persisting MEMORY_AND_DISK: {time.time() - start_time} seconds")

df.unpersist()

spark.stop()
