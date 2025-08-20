from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FilterMultipleConditions").getOrCreate()

data = [
    (1, "A", 100),
    (2, "B", 200),
    (3, "A", 150),
    (4, "C", 300),
    (5, "B", 250)
]
df = spark.createDataFrame(data, ["id", "category", "value"])

filtered_df = df.filter((col("category") == "A") & (col("value") > 120))

filtered_df.show()

spark.stop()
