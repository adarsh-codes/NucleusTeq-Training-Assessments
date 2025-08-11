#  Implement a Spark job to calculate total sales per product from a sales dataset.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Total Sales Per Product") \
    .getOrCreate()

sales_data = [("ProductA", 100),
              ("ProductB", 200),
              ("ProductA", 150),
              ("ProductC", 300),
              ("ProductB", 100),
              ("ProductC", 200),
              ("ProductA", 50),
              ("ProductB", 300)
              ]

df = spark.createDataFrame(sales_data, ["product", "sales_amount"])

df_grouped = df.groupBy("product").sum("sales_amount")

df_grouped = df_grouped.withColumnRenamed("sum(sales_amount)", "total_sales")

df_grouped.show()