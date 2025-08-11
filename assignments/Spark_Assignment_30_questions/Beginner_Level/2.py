# 2. Implement a Spark program to filter lines containing a specific keyword.

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Filter Lines with Keyword") \
    .master("local[*]") \
    .getOrCreate()


rdd = spark.sparkContext.textFile("1.txt")

print("Enter a keyword to filter lines:")
keyword = input().strip()

filtered_lines = rdd.filter(lambda line: keyword.lower() in line.lower())

print(f"Lines containing the keyword '{keyword}':", len(filtered_lines.collect()))
