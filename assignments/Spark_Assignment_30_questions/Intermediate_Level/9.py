# Write a Spark application to sort data by a numeric column in descending order.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Sort Data by Numeric Column") \
    .getOrCreate()

data = [(1, "Alice", 34),
        (2, "Bob", 23),
        (3, "Cathy", 45),
        (4, "David", 29),
        (5, "Eve", 31)]

columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)

df = df.sort(df.age.desc())

df.show()