from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IrisDataFormats").getOrCreate()

df = spark.read.option("header", "true").csv("file:///C:/demo/iris.csv")

df.write.mode("overwrite").parquet("file:///C:/demo/iris_parquet")
df.write.mode("overwrite").json("file:///C:/demo/iris_json")
df.write.mode("overwrite").orc("file:///C:/demo/iris_orc")

df_parquet = spark.read.parquet("file:///C:/demo/iris_parquet")
df_json = spark.read.json("file:///C:/demo/iris_json")  
df_orc = spark.read.orc("file:///C:/demo/iris_orc")

print("Parquet DataFrame:")
df_parquet.show()   
print("JSON DataFrame:")
df_json.show()
print("ORC DataFrame:")
df_orc.show()

input("Press Enter to exit...")