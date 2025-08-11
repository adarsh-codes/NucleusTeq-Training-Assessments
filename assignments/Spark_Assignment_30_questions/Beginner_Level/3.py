# 3. Write a Spark job to count occurrences of each character in a text file.

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("CharacterCount") \
    .getOrCreate()


rdd = spark.sparkContext.textFile("1.txt")
character_counts = rdd.flatMap(lambda line: list(line.lower())) \
    .map(lambda char: (char, 1)) \
    .reduceByKey(lambda a, b: a + b)

print("Character counts:")

for char, count in character_counts.collect():
    print(f"'{char}': {count}")

input("Press Enter to exit...")
