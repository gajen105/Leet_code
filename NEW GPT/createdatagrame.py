from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, dense_rank, explode, split
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("AvgSalaryByDept").getOrCreate()

employees_data = [
    (101, "Alice", 10),  # Match
    (102, "Bob", 20),    # Match
    (103, "Charlie", 10),# Match
    (104, "David", 30),  # Match
    (105, "Eve", 50),    # No Department Match (Orphan)
    (106, "Frank", 20),  # Match
    (107, "Grace", None) # Null dept_id
]

employees_df = spark.createDataFrame(
    employees_data,
    schema=["id", "name", "department", "salary"]
)

# salary_stats_df  = employees_df.groupBy("department")\
#                             .agg(sum("salary").alias("Total_salary"),
#                                  avg("salary").alias("avarage_salary"))
# salary_stats_df .show()

# w = Window().partitionBy('department').orderBy(col("salary").desc)
# second_highest_salary_df  = employees_df.withColumn("rnk", dense_rank().over(w)).filter(col("rnk")==2)
# second_highest_salary_df .show()


# --- 2. DEPARTMENTS DataFrame ---
department_data = [
    (10, "Sales"),
    (20, "Marketing"),
    (30, "HR"),
    (40, "Finance") # No Employee Match (Unused)
]
department_cols = ["dept_id", "dept_name"]

departments_df = spark.createDataFrame(department_data, department_cols)

employees_without_department_df = employees_df.join(departments_df, on='dept_id', how='left_anti')
employees_without_department_df.show()

# --- 2. Sample Data ---
order_data = [
    (1001, 1, "North", 150.50),
    (1002, 2, "South", 200.00),
    (1003, 1, "North", 75.25),
    (1004, 3, "East", 500.00),
    (1005, 4, "West", 125.75),
    (1006, 2, "South", 300.00),
    (1007, 5, "North", 90.00),
    (1008, 6, "East", 100.00),
    (1009, 3, "East", 450.50),
    (1010, 7, "West", 80.00),
    (1011, 8, "South", 600.00) # High-value order
]
columns = ['order_id', 'customer_id', 'region', 'amount']
# --- 3. Create the DataFrame ---
orders_df = spark.createDataFrame(data=order_data, schema=columns)

orders_df.cache()

orders_df.count() 

total_sales_per_region_df = orders_df.groupBy("region").agg(sum(col("amount")).alias("total_sales_amount"))

stream_df = spark.readStream \
                 .format("text") \
                 .load("C:\Users\gjndr\Pictures\Camera Roll")

word_df = stream_df.select( explode(split(stream_df.value, " ")).alias('word'))

word_count_df = word_df.groupBy("word").count()

query = word_count_df.writeStream \
                    .outputMode("complete") \
                    .format("console")\
                    .start()
query.awaitTermination()
