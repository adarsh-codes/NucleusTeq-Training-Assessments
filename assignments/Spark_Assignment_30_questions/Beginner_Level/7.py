# Implement a Spark job to group data by a column and count rows per group

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDDGroupCount").getOrCreate()

data = [
    ("Ansh", "Maths", 85),
    ("Ansh", "Science", 90),
    ("Ansh", "English", 88),
    ("John", "Maths", 78),
    ("John", "Science", 82),
    ("John", "English", 80),
    ("Prince", "Maths", 92),
    ("Prince", "Science", 95),
    ("Prince", "English", 89),
    ("Emma", "Maths", 75),
    ("Emma", "Science", 80),
    ("Emma", "English", 78)
]

rdd = spark.sparkContext.parallelize(data)

name_counts = rdd.map(lambda row: (row[0], 1))

counts_by_name = name_counts.reduceByKey(lambda a, b: a + b)

for name, count in counts_by_name.collect():
    print(f"{name}: {count}")
