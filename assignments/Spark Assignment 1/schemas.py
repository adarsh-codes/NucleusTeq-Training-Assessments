import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

os.environ["PYSPARK_PYTHON"] = "C:/demo/venv310/Scripts/python.exe"

spark = SparkSession.builder \
    .appName("SchemaExample") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

data = [("Alice", 30, "PH"), ("Bob", 25, "NY"), ("Charlie", 35, "LA")]
df = spark.createDataFrame(data, schema=schema)
df.show()

input("Press Enter to exit...")
