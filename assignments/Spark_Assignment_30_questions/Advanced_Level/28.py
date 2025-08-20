from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AccumulatorExample").getOrCreate()

even_count = spark.sparkContext.accumulator(0)

rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def count_even_numbers(x):
    global even_count
    if x % 2 == 0:
        even_count.add(1)


rdd.foreach(count_even_numbers)

print(f"Total even numbers: {even_count.value}")

spark.stop()
