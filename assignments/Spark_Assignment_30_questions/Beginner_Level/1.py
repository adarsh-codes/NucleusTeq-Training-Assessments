# 1. Create a Spark application to count words in a text file.

import re
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("WordCount") \
    .master("local[*]") \
    .getOrCreate()

input_path = "./1.txt"

rdd = spark.sparkContext.textFile(input_path)

word_counts = (
    rdd
    .flatMap(lambda line: re.findall(r"\b\w+\b", line.lower()))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
    .sortBy(lambda x: x[1], ascending=False) 
)

for word, count in word_counts.collect():
    print(word, count)

input("Press Enter to exit...")
