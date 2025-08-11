from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql import functions as F

spark = SparkSession.builder \
    .appName("Moving Average Calculation") \
    .getOrCreate()

data = [
    ("Adarsh", 10),
    ("Adarsh", 20),
    ("Admon", 30), 
    ("Adaah", 40),
    ("Adush", 50),
    ("Adush", 60),
]

df = spark.createDataFrame(data, ["Name", "Value"])

window_spec = Window.partitionBy("Name").rowsBetween(-2, 0)

df_with_moving_avg = df.withColumn(
    "moving_avg",
    F.avg("Value").over(window_spec)
)

df_with_moving_avg.show()

spark.stop()
