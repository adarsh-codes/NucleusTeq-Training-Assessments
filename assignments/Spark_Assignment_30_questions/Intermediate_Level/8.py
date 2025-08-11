# Create a Spark program to remove duplicates from a dataset.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Remove Duplicates") \
    .getOrCreate()


data = [("Alice", 1), ("Bob", 2), ("Alice", 1), ("Charlie", 3),
        ("Bob", 2), ("David", 4), ("Eve", 5), ("Charlie", 3)]

df = spark.createDataFrame(data, ["Name", "ID"])

removed_duplicates_df = df.dropDuplicates()

removed_duplicates_df.show()