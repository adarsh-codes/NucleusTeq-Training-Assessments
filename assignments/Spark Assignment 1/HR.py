# Problem: you have a dataframe with columns empid, empname, salary, department.
# You need to write this dataframe on HDFS but before writing you need to decrease the salary of all employees of the HR department by 10%.

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

os.environ['PYSPARK_PYTHON'] = 'C:/demo/venv310/Scripts/python.exe'

spark = SparkSession.builder \
    .appName("HR Data Processing") \
    .getOrCreate()


data = [
    (1, "Alice", 50000, "HR"),
    (2, "Bob", 60000, "Engineering"),
    (3, "Charlie", 70000, "HR"),
    (4, "David", 80000, "Marketing"),
    (5, "Eve", 90000, "HR"),
    (6, "Frank", 100000, "Engineering"),
    (7, "Grace", 110000, "HR"),
    (8, "Heidi", 120000, "Marketing"),
    (9, "Ivan", 130000, "HR"),
    (10, "Judy", 140000, "Engineering")]

columns = ["empid", "empname", "salary", "department"]

df = spark.createDataFrame(data, columns)

df_updated = df.withColumn(
    "salary",
    when(col("department") == "HR", col("salary") * 0.9).otherwise(col("salary"))
)

print("Updated DataFrame with adjusted salaries:")
df_updated.write.mode("overwrite").parquet("hdfs_simulated/employees")
df_read = spark.read.parquet("hdfs_simulated/employees").orderBy(col("empid"))
df_read.explain()
df_read.show()

input("Enter to exit...")
