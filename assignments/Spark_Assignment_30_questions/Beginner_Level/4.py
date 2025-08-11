# Load a CSV file using Spark and print the schema.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV Loader") \
    .getOrCreate()

csv_file = spark.read.csv("customers-1000.csv", header=True, inferSchema=True)

csv_file.printSchema()