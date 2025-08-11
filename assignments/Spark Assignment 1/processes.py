# Problem: find the process that took the maximum time to execute in hours.
# (dataset - cols [process_id,process_name, strt_dt_time, end_dt_time])

import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

os.environ["PYSPARK_PYTHON"] = "C:/demo/venv310/Scripts/python.exe"

spark = SparkSession.builder \
    .appName("ProcessDurationExample") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

data = [
    (1, "ProcessA", "2023-10-01 08:00:00", "2023-10-02 10:30:00"),
    (2, "ProcessB", "2023-10-01 09:00:00", "2023-10-05 11:00:00"),
    (3, "ProcessC", "2023-10-01 07:30:00", "2023-10-01 09:00:00"),
    (4, "ProcessD", "2023-10-01 10:00:00", "2023-10-01 12:00:00")
]
df = spark.createDataFrame(data, ["process_id", "process_name", "strt_dt_time", "end_dt_time"])
df = df.withColumn("time_taken_hours", round((col("end_dt_time").cast("timestamp").cast("long") - col("strt_dt_time").cast("timestamp").cast("long")) / 3600, 2))
df = df.orderBy(col("time_taken_hours").desc())
df.show(1)
input("Press Enter to exit...")
