from pyspark.sql.functions import explode, split
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("TokenizeWords").getOrCreate()

data = [("This is a sentence",), ("This is another sentence",)]
df = spark.createDataFrame(data, ["sentence"])

df_words = df.select(explode(split(F.col("sentence"), " ")).alias("word"))

df_word_count = df_words.groupBy("word").count()
df_word_count.show()
