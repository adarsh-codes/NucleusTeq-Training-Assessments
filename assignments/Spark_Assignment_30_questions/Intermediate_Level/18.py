# Implement a Spark job to unpivot a wide dataset into long format.

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder \
    .appName("Unpivot Example") \
    .getOrCreate()

data = [
    ("Alice", 10, 20, 30),
    ("Bob", 15, 25, 35),
    ("Cathy", 20, 30, 40)
]

columns = ["Name", "Score1", "Score2", "Score3"]

df = spark.createDataFrame(data, columns)

unpivoted_df = df.select(
    "Name",
    expr("stack(3, 'Score1', Score1, 'Score2', Score2, 'Score3', Score3) as (ScoreType, ScoreValue)")
)

unpivoted_df.show()
