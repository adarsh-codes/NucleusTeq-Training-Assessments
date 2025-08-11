# Create a Spark job to pivot a dataset based on a category column.

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("Pivot Dataset") \
    .getOrCreate()

data = [
    ("Alice", "Math", 85),
    ("Alice", "Science", 90),
    ("Bob", "Math", 75),
    ("Bob", "Science", 80),
    ("Charlie", "Math", 95),
    ("Charlie", "Science", 88),
]

df = spark.createDataFrame(data, ["name", "subject", "score"])

pivoted_df = df.groupBy("name").pivot("subject").agg(F.first("score"))

pivoted_df.show()
