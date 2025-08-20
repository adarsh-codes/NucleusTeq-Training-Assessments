from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SimpleETL").getOrCreate()

df = spark.read.csv("marksheet.csv", header=True, inferSchema=True)

df_transformed = df.filter(col("English") > 80)

df_transformed.write.mode("overwrite").parquet("english_marks_parquet")

read_parquet_df = spark.read.parquet("output_parquet")
read_parquet_df.show()