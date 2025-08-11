from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Stats_CSV").getOrCreate()

rdd = spark.sparkContext.textFile("./Beginner_Level/customers-1000.csv")

header = rdd.first()
rdd_no_header = rdd.filter(lambda line: line != header)

index_rdd = rdd_no_header.map(lambda line: int(line.split(",")[0]))

count = index_rdd.count()
total = index_rdd.sum()
minimum = index_rdd.min()
maximum = index_rdd.max()
average = total / count

print(f"Average: {average}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")
