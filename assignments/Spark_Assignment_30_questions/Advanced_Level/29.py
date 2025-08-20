from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, lit, rand, col

spark = SparkSession.builder.appName("SaltingSkewedData").getOrCreate()

data = [("A", 1), ("A", 2), ("A", 3), ("B", 4), ("B", 5), ("C", 6)]
df = spark.createDataFrame(data, ["key", "value"])

num_salts = 5

df_salted = df.withColumn("salt", (rand() * num_salts).cast("int"))

df_salted = df_salted.withColumn("salted_key", concat(col("key"), lit("_"), col("salt")))

df_salted.show(truncate=False)

spark.stop()
