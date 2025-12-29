# 🔥 PySpark & Apache Spark – 180 Interview Questions (Topic-wise)

Structured for **6–8 years Data Engineer / Spark / Databricks roles**

Each topic contains:
- ✅ Core Questions
- 🔍 Deep / Follow-up Questions
- 🧠 Scenario-Based Questions

---

## 1️⃣ Spark & PySpark Fundamentals (15)

### ✅ Core
1. What is Apache Spark?
2. What is PySpark?
3. Spark vs Hadoop MapReduce
4. Spark vs PySpark
5. Why is Spark faster than MapReduce?
6. What are Spark applications?
7. What is a Spark job?
8. What is a Spark stage?
9. What is a Spark task?
10. Explain Spark driver and executors

### 🔍 Deep / Follow-up
11. How does PySpark communicate with JVM?
12. What is the role of SparkContext vs SparkSession?
13. How does Spark handle fault tolerance?
14. Explain Spark DAG
15. What happens internally when you submit a Spark job?

---

## 2️⃣ Distributed Computing Basics (10)

### ✅ Core
16. What is distributed computing?
17. What is data partitioning?
18. What is parallelism in Spark?
19. What is data locality?
20. What is cluster computing?

### 🔍 Deep / Follow-up
21. How does Spark decide the number of tasks?
22. What is skewed data?
23. What is shuffle?
24. What causes slow shuffles?
25. How does Spark recover from executor failure?

---

## 3️⃣ Spark Architecture (15)

### ✅ Core
26. Explain Spark architecture
27. What is a cluster manager?
28. Spark Standalone vs YARN vs Kubernetes
29. What is an executor?
30. What is a worker node?

### 🔍 Deep / Follow-up
31. How does the driver communicate with executors?
32. How is memory divided in Spark?
33. What is BlockManager?
34. How does Spark handle heartbeats?
35. Explain Spark application lifecycle

### 🧠 Scenario-Based
36. Your Spark job fails due to executor memory — how do you debug?
37. How would you design Spark on Kubernetes?

---

## 4️⃣ RDDs (Resilient Distributed Datasets) (15)

### ✅ Core
38. What is an RDD?
39. RDD vs DataFrame vs Dataset
40. Why are RDDs immutable?
41. How do you create an RDD?
42. What are RDD transformations?
43. What are RDD actions?

### 🔍 Deep / Follow-up
44. What is RDD lineage?
45. What is narrow vs wide transformation?
46. What is RDD persistence?
47. How does RDD fault tolerance work?
48. When should you use RDDs today?

### 🧠 Scenario-Based
49. Debugging an RDD job running slower than expected
50. Handling huge text files using RDDs

---

## 5️⃣ DataFrames & Spark SQL (20)

### ✅ Core
51. What is a DataFrame?
52. How are DataFrames optimized?
53. Spark SQL vs Hive
54. What is Catalyst Optimizer?
55. What is Tungsten?
56. How to create a DataFrame in PySpark?
57. Schema inference vs explicit schema
58. select vs withColumn
59. What is explode?
60. What is a UDF?

### 🔍 Deep / Follow-up
61. Logical plan vs physical plan
62. What is predicate pushdown?
63. How does Spark optimize joins?
64. What is Cost-Based Optimizer (CBO)?
65. What is WholeStageCodeGen?

### 🧠 Scenario-Based
66. Handling schema drift
67. Optimizing a slow Spark SQL query
68. Migrating Hive queries to Spark SQL
69. UDF vs built-in functions
70. Debugging incorrect query results

---

## 6️⃣ Transformations & Actions (10)

### ✅ Core
71. What are transformations?
72. What are actions?
73. What is lazy evaluation in Spark?
74. Examples of transformations
75. Examples of actions

### 🔍 Deep / Follow-up
76. How does lazy evaluation improve performance?
77. How do you force execution?
78. collect vs take
79. count vs countDistinct
80. Which actions trigger shuffle?

---

## 7️⃣ Joins & Aggregations (15)

### ✅ Core
81. Types of joins in Spark
82. Inner vs outer join
83. What is a broadcast join?
84. groupBy vs reduceByKey
85. agg vs groupBy

### 🔍 Deep / Follow-up
86. How does Spark choose join strategy?
87. What is sort-merge join?
88. What is shuffle hash join?
89. What is join skew?
90. What is salting?

### 🧠 Scenario-Based
91. Optimizing large fact-dimension joins
92. Handling skewed keys
93. Broadcasting large tables accidentally
94. Join performance tuning
95. Debugging wrong aggregation results

---

## 8️⃣ Partitioning & Bucketing (10)

### ✅ Core
96. What is partitioning?
97. repartition vs coalesce
98. Hash partitioning
99. Range partitioning
100. What is bucketing?

### 🔍 Deep / Follow-up
101. When does repartition cause shuffle?
102. What is partition pruning?
103. How partition size impacts performance
104. Bucketing vs partitioning
105. Partitioning best practices

---

## 9️⃣ Caching & Persistence (10)

### ✅ Core
106. What is caching?
107. cache vs persist
108. Storage levels
109. MEMORY_ONLY vs MEMORY_AND_DISK
110. When should you cache?

### 🔍 Deep / Follow-up
111. How caching works internally
112. What happens when memory is full?
113. Cache invalidation
114. Impact of caching on shuffle
115. Debugging cache misuse

---

## 🔟 Spark Performance Optimization (15)

### ✅ Core
116. How do you optimize Spark jobs?
117. Common Spark performance issues
118. What is data skew?
119. What is shuffle optimization?
120. Executor memory tuning

### 🔍 Deep / Follow-up
121. spark.sql.shuffle.partitions
122. Executor vs core sizing
123. Adaptive Query Execution (AQE)
124. Speculative execution
125. Garbage collection tuning

### 🧠 Scenario-Based
126. Job slow only in production
127. OOM errors
128. Skewed join optimization
129. Too many small files
130. SLA-based Spark tuning

---

## 1️⃣1️⃣ Spark Streaming & Structured Streaming (15)

### ✅ Core
131. What is Spark Streaming?
132. DStreams vs Structured Streaming
133. Micro-batch vs continuous processing
134. What is watermark?
135. What is window operation?

### 🔍 Deep / Follow-up
136. Exactly-once semantics
137. Late data handling
138. Stateful streaming
139. Checkpointing
140. Trigger types

### 🧠 Scenario-Based
141. Real-time Kafka pipeline
142. Handling late events
143. Restarting failed streams
144. Streaming job scaling
145. Streaming data loss issue

---

## 1️⃣2️⃣ File Formats & Data Sources (10)

### ✅ Core
146. Parquet vs ORC vs Avro
147. JSON vs CSV performance
148. What is columnar storage?
149. Compression types
150. Schema evolution

### 🔍 Deep / Follow-up
151. Predicate pushdown with Parquet
152. Small file problem
153. mergeSchema impact
154. Partitioned reads
155. Handling corrupt records

---

## 1️⃣3️⃣ Delta Lake (10)

### ✅ Core
156. What is Delta Lake?
157. Delta vs Parquet
158. ACID transactions
159. Time travel
160. Schema enforcement

### 🔍 Deep / Follow-up
161. Delta merge (upsert)
162. Vacuum
163. Optimize & Z-Order
164. Concurrency control
165. Delta streaming

---

## 1️⃣4️⃣ Deployment, Debugging & Best Practices (15)

### ✅ Core
166. How do you submit a Spark job?
167. spark-submit parameters
168. Logging in Spark
169. Debugging Spark failures
170. PySpark best practices

### 🔍 Deep / Follow-up
171. Python serialization issues
172. Executor lost errors
173. Broadcast timeout issues
174. Version compatibility
175. CI/CD for Spark jobs

### 🧠 Scenario-Based
176. Spark job fails after deployment
177. Cluster scaling issue
178. Spark job retry logic
179. Production monitoring strategy
180. Designing enterprise-grade Spark pipelines

---

# 🔥 PySpark Coding Questions (20) – Interview Ready

Level: **Mid to Senior Data Engineer (5–8 Years)**  
Focus: **DataFrames, SQL, Performance, Real-World Scenarios**

---

## 1️⃣ Basic DataFrame Operations

### 1. Create a DataFrame with explicit schema
Create a PySpark DataFrame for employee data with columns:
`emp_id (int), name (string), dept (string), salary (int), join_date (date)`  
Load data from a CSV file.

---

### 2. Select and rename columns
Select `emp_id`, `name`, and `salary` from a DataFrame and rename `salary` to `monthly_salary`.

---

### 3. Filter rows using multiple conditions
Filter employees whose salary is greater than 50,000 and department is either `IT` or `HR`.

---

## 2️⃣ Aggregations & Grouping

### 4. Group by and aggregate
Find the **average salary per department**.

---

### 5. Count distinct values
Find the **number of unique employees per department**.

---

### 6. Top N records per group
Find the **top 2 highest-paid employees per department** using window functions.

---

## 3️⃣ Joins

### 7. Inner join two DataFrames
Join `employees` and `departments` DataFrames using `dept_id`.

---

### 8. Find unmatched records
Find employees who **do not belong to any department**.

---

### 9. Optimize large-small join
Perform a join where `departments` is small and `employees` is large.  
Ensure the join is optimized.

---

## 4️⃣ Window Functions

### 10. Running total
Calculate the **running total salary per department ordered by join date**.

---

### 11. Rank vs Dense Rank
Assign `rank` and `dense_rank` to employees based on salary within each department.

---

## 5️⃣ Date & Time Operations

### 12. Date difference
Calculate the **number of days each employee has worked** till today.

---

### 13. Monthly aggregation
Calculate **total salary paid per month**.

---

## 6️⃣ Data Cleaning & Transformation

### 14. Handle null values
Replace null salary with department-wise average salary.

---

### 15. Explode nested data
Given a column `skills = ["Python", "Spark", "SQL"]`, explode it into multiple rows.

---

## 7️⃣ Performance & Optimization

### 16. Repartition vs coalesce
Repartition a DataFrame into 10 partitions and then reduce it to 5 partitions efficiently.

---

### 17. Cache reusable DataFrame
Cache a DataFrame used multiple times in downstream transformations and explain when to unpersist.

---

## 8️⃣ File Formats & I/O

### 18. Read and write Parquet
Read Parquet data, filter records, and write the output partitioned by `dept`.

---

### 19. Handle small files problem
Write data in a way that avoids creating too many small files.

---

## 9️⃣ Real-World Scenario

### 20. Deduplicate records
Given a DataFrame with duplicate employee records, keep **only the latest record per emp_id** based on `update_timestamp`.

---

## ✅ Interview Tip
For each question, be prepared to explain:
- Why you chose a particular approach
- Shuffle impact
- Partitioning strategy
- Performance trade-offs

---

📌 Want next?
- ✔ **Solutions for all 20 questions**
- ✔ **PySpark SQL-only versions**
- ✔ **Databricks-style coding round**
- ✔ **Mock coding interview (step-by-step)**

Just tell me 👍
