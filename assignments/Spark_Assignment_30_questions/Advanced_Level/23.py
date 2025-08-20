from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Correlation").getOrCreate()

data = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
df = spark.createDataFrame(data, ["column1", "column2"])

correlation = df.stat.corr("column1", "column2")

print(f"Correlation between column1 and column2: {correlation}")

spark.stop()
