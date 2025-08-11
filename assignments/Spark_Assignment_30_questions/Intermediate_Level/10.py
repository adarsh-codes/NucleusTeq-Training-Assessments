# Load JSON data in Spark and extract specific fields.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Load JSON Data") \
    .getOrCreate()

df = spark.read.option("multiline", True).json("./Intermediate_Level/example.json")

selected_df = df.select("name", "version")

selected_df.show()