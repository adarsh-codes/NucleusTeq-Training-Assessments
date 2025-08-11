import os
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import col, lag, round

os.environ["PYSPARK_PYTHON"] = "C:/demo/venv310/Scripts/python.exe"

spark = SparkSession.builder \
    .appName("SchemaExample") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

# Problem: Calculate percentage revenue increased per year (dataset - cols [id,org_id, year, revenue])

data = [(1, 100, 2022, 1000), (2, 100, 2023, 1500), (3, 101, 2022, 2000), (4, 101, 2023, 2200)]
df = spark.createDataFrame(data, ["id", "org_id", "year", "revenue"])

w = Window.partitionBy("org_id").orderBy("year")
df = df.withColumn("prev_revenue", lag("revenue").over(w))
df = df.withColumn("percent_increase", round(((col("revenue") - col("prev_revenue")) / col("prev_revenue")) * 100, 2))
df.show()

input("Press Enter to exit...")
