# Implement a Spark program to filter out null or empty values from a dataset.

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("Filter Null or Empty Values") \
    .getOrCreate()

data = [
    ("Alice", 25),
    ("Bob", None),  
    ("Charlie", 30),
    ("David", None),
    ("Eve", 22),
    ("", 28),
]

df = spark.createDataFrame(data, ["name", "age"])

filtered_df = df.filter(
    (F.col("name").isNotNull()) & (F.col("name") != "") &
    (F.col("age").isNotNull())
)


filtered_df.show()