from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder \
    .appName("Running Total of Sales") \
    .getOrCreate()

data = [
    ("2025-08-01", 100),
    ("2025-08-02", 150),
    ("2025-08-03", 200),
    ("2025-08-04", 50),
    ("2025-08-05", 75)
]

df = spark.createDataFrame(data, ["date", "sales_amount"])

window_spec = Window.orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_with_running_total = df.withColumn(
    "running_total",
    F.sum("sales_amount").over(window_spec)
)

df_with_running_total.show()

spark.stop()
