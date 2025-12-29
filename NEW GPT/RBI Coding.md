Perfect 👍
Below is a **PURE CODING QUESTION SET**, **topic-wise**, **RBI-oriented**, and **interview-relevant**.

👉 These are **NOT MCQs or theory**
👉 These are **hands-on / whiteboard / practical coding questions**
👉 Difficulty ranges from **basic → senior-level**, exactly how RBI interviews test

You can treat this as your **CODING PRACTICE SYLLABUS**.

---

# 1️⃣ Core Data Engineering Foundations – Coding / Design Tasks

1. Design a simple **batch data pipeline flow** (pseudo-code) to:

   * Read data
   * Validate records
   * Store clean vs rejected data separately

2. Write pseudo-code to:

   * Ingest daily transaction files
   * Ensure idempotency (no duplicate processing)

3. Design logic to:

   * Compare source record count vs target record count
   * Raise alert if mismatch

---

# 2️⃣ SQL & RDBMS – CODING QUESTIONS (🔥 RBI FAVORITE)

### Basic → Advanced

1. Find **duplicate records** in a table.
2. Fetch **second highest salary**.
3. Remove duplicate rows but keep one.
4. Find employees earning more than department average.
5. Get **top 3 salaries per department** (window function).
6. Find records present in Table A but not in Table B.
7. Calculate running total using window functions.
8. Find consecutive login days for a user.
9. Pivot rows to columns using SQL.
10. Identify gaps in sequence numbers.
11. Write SQL to detect **deadlock-prone queries** (conceptual + SQL).
12. Optimize a slow query given indexes.
13. Write SQL to implement **SCD Type 2**.
14. Partition a table and query efficiently.
15. Write SQL to reconcile two tables (source vs target).

---

# 3️⃣ Python (Core + Practical) – CODING QUESTIONS

### Core Python

1. Reverse a string without using slicing.
2. Find frequency of characters in a string.
3. Check if two strings are anagrams.
4. Find duplicate elements in a list.
5. Flatten a nested list.
6. Implement shallow vs deep copy example.
7. Write a generator to read large files line by line.
8. Implement custom exception handling.
9. Count word frequency from a file.
10. Merge two dictionaries.

### Data Engineering Focus

11. Read a CSV file and validate schema.
12. Write Python code to remove duplicate records.
13. Implement retry logic for a failed API call.
14. Write a script to log errors to a file.
15. Process large JSON file efficiently.

---

# 4️⃣ Apache Spark & PySpark – CODING QUESTIONS (🔥🔥 MOST IMPORTANT)

### PySpark DataFrame Coding

1. Read CSV/Parquet into DataFrame.
2. Filter records based on conditions.
3. Add a derived column.
4. Remove duplicates.
5. Perform groupBy + aggregation.
6. Join two DataFrames.
7. Find top N records per group.
8. Handle null values.
9. Broadcast join example.
10. Repartition vs Coalesce usage.
11. Detect and handle data skew.
12. Cache a DataFrame and explain why.
13. Write data partitioned by date.
14. Convert DataFrame to RDD and back.
15. Implement SCD Type 2 using PySpark.

### Optimization Tasks

16. Optimize a slow Spark job.
17. Reduce small files while writing output.

---

# 5️⃣ Databricks & Delta Lake – CODING TASKS

1. Create a Delta table.
2. Write data to Delta Lake.
3. Perform **MERGE INTO (Upsert)**.
4. Enable schema evolution.
5. Time Travel query.
6. Delete records and restore using Time Travel.
7. Optimize a Delta table.
8. Implement Z-Ordering.
9. Handle duplicate records in Delta.
10. Compare Parquet vs Delta writes.

---

# 6️⃣ ETL / ELT & Pipeline Design – CODING / LOGIC

1. Write ETL logic for:

   * Source → Staging → Target

2. Implement incremental load logic.

3. Handle late-arriving data.

4. Write validation logic for:

   * Null checks
   * Range checks

5. Implement audit columns (created_at, updated_at).

6. Design reprocessing logic.

7. Build error-handling framework.

8. Implement SCD Type 1 & Type 2 logic.

---

# 7️⃣ Apache Airflow – CODING QUESTIONS

1. Write a simple DAG.
2. Define task dependencies.
3. Use PythonOperator.
4. Schedule DAG using cron.
5. Implement retry logic.
6. Add SLA to a task.
7. Use XCom to pass data.
8. Implement branching.
9. Backfill a DAG.
10. Handle DAG failure alerting.

---

# 8️⃣ AWS Data Engineering – CODING / CONFIG TASKS

1. Upload file to S3 using Python (boto3).
2. Read data from S3 in Spark.
3. Write partitioned data to S3.
4. Create AWS Glue Job (logic).
5. Create Glue Crawler.
6. Query data using Athena.
7. Redshift COPY command.
8. Optimize Redshift table with sort/dist keys.
9. Implement IAM role access.
10. Encrypt data at rest and transit (conceptual + config).

---

# 9️⃣ Data Modeling & Architecture – LOGIC / DESIGN

1. Design star schema for banking transactions.
2. Convert OLTP schema to OLAP.
3. Implement SCD Type 2 schema.
4. Design fact & dimension tables.
5. Handle historical data storage.
6. Schema evolution handling.

---

# 🔟 Data Governance & Security – CODING / LOGIC

1. Mask PII fields in SQL.
2. Encrypt sensitive columns.
3. Implement role-based access.
4. Audit data changes.
5. Log data access events.
6. Data validation framework design.

---

# 1️⃣1️⃣ Kafka / Streaming – CODING (Conceptual + Light)

1. Kafka producer pseudo-code.
2. Kafka consumer pseudo-code.
3. Offset management logic.
4. Exactly-once processing logic.
5. Streaming vs batch decision logic.

---

# 1️⃣2️⃣ DevOps, CI/CD & Agile – PRACTICAL TASKS

1. Write Git branching workflow.
2. Create CI pipeline steps for ETL.
3. Deployment rollback strategy.
4. Version control for data pipelines.
5. Monitoring & alerting logic.

---

# 1️⃣3️⃣ Visualization & Analytics Support – DATA TASKS

1. Prepare aggregated dataset for dashboard.
2. Optimize SQL for reporting.
3. Ensure metric consistency.
4. Handle late data in reports.
5. Reconcile dashboard numbers.

---

## ✅ HOW TO USE THIS EFFECTIVELY (IMPORTANT)

👉 Pick **one topic**
👉 I will:

* Ask you **coding questions**
* Review your solution
* Optimize it
* Convert it into **RBI-ready answer**

### 🔥 NEXT STEP

Reply with:

> **“Start coding interview for Topic X”**

Example:

* *Start coding interview for SQL*
* *Start coding interview for PySpark*

We’ll do **real interview simulation**, not just answers 💪🏦
