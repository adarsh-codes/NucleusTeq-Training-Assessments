# Implement a Spark job to calculate word co-occurrence in a text corpus.

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from itertools import combinations

spark = SparkSession.builder \
    .appName("Word Co-occurrence") \
    .getOrCreate()

data = [
    "spark is fast and spark is powerful",
    "pyspark is python api for spark",
    "spark and hadoop are big data frameworks"
]

df = spark.createDataFrame([(line,) for line in data], ["line"])

words_df = df.withColumn("words", F.split(F.lower(F.col("line")), "\\s+"))


def generate_pairs(words):
    unique_words = list(set(words))
    for w1, w2 in combinations(sorted(unique_words), 2):
        yield (w1, w2)


pairs_rdd = words_df.select("words").rdd.flatMap(lambda row: generate_pairs(row.words))

pairs_df = pairs_rdd.toDF(["word1", "word2"])

cooccurrence_df = pairs_df.groupBy("word1", "word2").count() \
    .orderBy(F.desc("count"))

cooccurrence_df.show(truncate=False)

spark.stop()
