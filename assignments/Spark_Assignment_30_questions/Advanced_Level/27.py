from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName("BroadcastExample").getOrCreate()

lookup_data = [(1, "Category A"), (2, "Category B"), (3, "Category C")]
lookup_df = spark.createDataFrame(lookup_data, ["id", "category"])

main_data = [(1, 100), (2, 200), (3, 300), (4, 400)]
main_df = spark.createDataFrame(main_data, ["id", "value"])

result_df = main_df.join(broadcast(lookup_df), on="id", how="left")

result_df.show()

spark.stop()
