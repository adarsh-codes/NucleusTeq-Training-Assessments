# Use Spark to convert a CSV file to Parquet format.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV to Parquet Conversion") \
    .getOrCreate()

df = spark.read.csv("customers-1000.csv", header=True, inferSchema=True)

df.write.parquet("customers-1000.parquet")

read_parquet = spark.read.parquet("customers-1000.parquet")
read_parquet.show()