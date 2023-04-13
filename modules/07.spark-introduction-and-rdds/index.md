---
Duration: 3 hours
---

# Introduction to Spark & RDDs

## What is Apache Spark?

- Fast (in-memory), distributed (parallel), general-purpose **cluster computing system** -   [spark.apache.org](https://spark.apache.org/docs/latest/index.html)
- **Open Source** project ([Apache Software Foundation](http://www.apache.org/))
- Strongly tied to the **Hadoop** ecosystem
- Written in **Scala** → runs in the JVM (Java Virtual Machine)
- Pick your language: **Scala, Python, R, SQL, Java**
- Spark transforms your code into **tasks** to run on the **cluster nodes**

## Spark in Hadoop ecosystem

![Hadoop ecosystem](./image/hadoop_ecosystem.png)

## Use cases

- Analyze / transform / apply ML models on:
  - Very **large datasets** (Extract, Transform and Load)
  - **Streaming** data (in near-real-time)
  - **Graphs** (network analysis)
- of structured (tables), semi-structured (JSON) or unstructured (text) data

## Spark ecosystem

![Spark ecosystem](./image/spark_ecosystem.png)

## Internals

Spark connects to cluster managers that **distribute resources** (RAM, CPU) to applications, running on a cluster:

- Hadoop **YARN**
- Apache Mesos
- Kubernetes
- Spark standalone

When you write the code and submit it, Spark:

1. Asks for resources to **create driver + executors**
2. Transforms the **code** into **tasks**
3. **Driver** sends **tasks** to **executors**
4. **Executors** send **status** to **driver**

![Spark internals](./image/spark_internals.png)

## Data structures

![Spark data structures](./image/spark_data_structures.PNG)

## Operations

2 types of **operations**:

- **Transformations**:
  - transform a Spark DataFrame/RDD into a new DataFrame/RDD
  - examples: `orderBy()`, `groupBy()`, `filter()`, `select()`, `join()`
- **Actions**:  
  - get the result
  - examples: `show()`, `take(10)`, `count()`, `collect()`, `save()`

**Lazy evaluation**: transformations triggered when action is called.

### API

Chain transformations and use the result with an action :

```Python
rdd = (
    sc.wholeTextFiles('hdfs://text/file/path')
    .map(lambda x: x.split(','))      #transformation
    .flatMap(...)                     #transformation
    .groupByKey(...)                  #transformation
)

rdd.take(10)      # action
```

When an action is run:

- Spark builds a **Directed Acyclic Graph (DAG)** of stages
- 1 **stage** = X **tasks** (1 by RDD partition)
- Tasks are sent to **executors**
- The end of one stage is conditioned by a **shuffle**

![Spark DAG](./image/spark_dag.png)

## RDDs: Resilient Distributed Datasets

### Properties

- A **fault-tolerant collection** of elements partitioned **across the nodes** of the cluster (parallelism)
- An element can be: string, array, dictionary, etc.
- An RDD is **immutable**
- Transformations: lambda expressions on  **key-value pairs**
- An RDD can be **persisted** in memory for reuse (avoid recomputing)
- Mostly load data from **HDFS** (or Hadoop-like file system)
- RDDs are **partitioned**:
  - **1 partition** = **1 block** = 128 MB in HDFS
  - **1 task** runs on **1 partition**
  - Default = 1 partition per CPU core

### Narrow and wide transformations

![Transformations](./image/narrow_wide_transformations.png)
