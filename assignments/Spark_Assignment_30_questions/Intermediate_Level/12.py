#  Create a Spark program to find the top 5 most frequent words in a text file


from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("Top 5 Most Frequent Words") \
    .getOrCreate()

read_file = spark.read.text("./Intermediate_Level/1.txt")

df = read_file.selectExpr("split(value, ' ') as words")

df = df.withColumn("words", F.explode("words")) \
    .groupBy("words") \
    .count() \
    .orderBy("count", ascending=False)

df.show(5)