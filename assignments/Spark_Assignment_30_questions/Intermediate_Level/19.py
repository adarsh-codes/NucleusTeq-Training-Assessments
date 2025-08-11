from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark Joins Example") \
    .getOrCreate()

data1 = [
    (1, "Alice", 29),
    (2, "Bob", 31),
    (3, "Charlie", 25),
    (4, "David", 35)
]

data2 = [
    (3, "HR"),
    (1, "Finance"),
    (5, "Marketing"),
    (2, "IT")
]

df1 = spark.createDataFrame(data1, ["id", "name", "age"])
df2 = spark.createDataFrame(data2, ["id", "department"])

inner_join_df = df1.join(df2, on="id", how="inner")
print("Inner Join Result:")
inner_join_df.show()

left_join_df = df1.join(df2, on="id", how="left")
print("Left Join Result:")
left_join_df.show()

right_join_df = df1.join(df2, on="id", how="right")
print("Right Join Result:")
right_join_df.show()

spark.stop()
