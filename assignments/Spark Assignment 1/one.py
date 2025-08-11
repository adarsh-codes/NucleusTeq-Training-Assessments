import os
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = "C:/demo/venv310/Scripts/python.exe"

spark = SparkSession.builder \
    .appName("WordCountSortedApp") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext

sc.setLogLevel("ERROR")

sample_data = [
    "Spark is a powerful engine for big data",
    "Big data requires powerful tools like Spark",
    "Spark and Python are a great combination",
    "Learning Spark RDD is a fundamental skill",
    "The engine is fast and the tools are great"
]

rdd = sc.parallelize(sample_data)

words_rdd = rdd.flatMap(lambda line: line.lower().split())

word_map_rdd = words_rdd.map(lambda word: (word, 1))

word_counts_rdd = word_map_rdd.reduceByKey(lambda count1, count2: count1 + count2)

counts_as_key_rdd = word_counts_rdd.map(lambda item: (item[1], item[0]))

sorted_rdd = counts_as_key_rdd.sortByKey(ascending=False)

final_results = sorted_rdd.collect()

print("--- Word Count Sorted by Frequency (Descending) ---")
for count, word in final_results:
    print(f"'{word}': {count}")

spark.stop()
print("--- SparkEnd ---")