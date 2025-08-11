from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDDJoinExample").getOrCreate()

data1 = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
data2 = [("Alice", "F"), ("Bob", "M"), ("David", "M")]

rdd1 = spark.sparkContext.parallelize(data1)
rdd2 = spark.sparkContext.parallelize(data2)

joined_rdd = rdd1.join(rdd2)

for record in joined_rdd.collect():
    print(record)
