---
duration: 3 hours
---

# Hadoop core: HDFS and YARN

## The Hadoop Ecosystem

- A stack of **Open Source softwares** offering all the functionalities needed to build a [Data Lake](https://en.wikipedia.org/wiki/Data_lake) and exploit the data stored in it. Most of the Hadoop projects are maintained by the [Apache Software Foundation](https://apache.org) and can be found on [their GitHub](https://github.com/apache).
- Nearly are built using **Java** or at least run in the **JVM** (Java Virtual Machine)
- Preferred execution environment: **Linux**

## Hadoop ecosystem projects

- Distributed Filesystem: HDFS
- Cluster Manager: YARN
- Execution Engines: MapReduce, Tez, Spark
- Warehouse / SQL: Hive
- NoSQL DB: HBase
- And other stuff

## Apache Hadoop core

- **HDFS:** Hadoop Distributed File System
- **YARN:** Yet Another Resource Negotiator
- **MapReduce:** Big Data applications framework

## What is HDFS?

The **Hadoop Distributed File System**:

- Data stored on **hundred/thousands of nodes**
- Data is **replicated**:
  - Avoid data loss
  - Optimize access
- Support **huge files**: typical size from GB to TB
- Focus on **high throughput** vs low latency
- **Unix-like** file system (tree + rwx permissions)

## Master / Slave architecture

- Master component coordinates workers
- Worker components do the job (compute)

Other distributed architectures?

## HDFS: Files storage

- One file is divided into **blocks**
  - 1 block = **128 MB** (max)
  - Each block is **replicated** (x3 by default)
- E.g. 1 file of 420 MB =
  - 3 blocks of 128 MB + 1 block of 36 MB
  - The file actually takes 1.26 GB of disk in the cluster

## HDFS: Architecture

- **NameNode** (= master): Handles file system metadata. For each file, it knows

  - The path of the file in HDFS
  - The blocks that compose the file
  - The position of each block in the cluster

- **DataNodes** (= workers):

  - Store the blocks on disks (hardware optimization)
  - Handle read/write operations

- **Secondary NameNode**: Builds HDFS checkpoints (= FSImage) from NameNode edit logs

## HDFS: Data replication example

<img src="https://hadoop.apache.org/docs/r1.2.1/images/hdfsdatanodes.gif" alt="HDSF blocks" style="zoom:75%;" />

## HDFS: Client interactions

<img src="https://hadoop.apache.org/docs/r3.1.0/hadoop-project-dist/hadoop-hdfs/images/hdfsarchitecture.png" alt="HDFS clients" style="zoom:75%;" />

## HDFS: Important properties

- **WORM** = Write Once Read Many: no update on files
- **Rack awareness**
- NameNode stores all the metadata in RAM => **small files problem**

## HDFS: Sum up

Components:

- **NameNode**: tracks blocks/files in the cluster
- **DataNode**: stores blocks + handles read/write operations
- **Secondary NameNode**: builds checkpoints (FSImage) based on edit logs

What is wrong with this architecture? => **SPOF (Single Point of Failure)**

## High Availability

High Availability: more than 1 master (1 **active** + N **standby**)

- Avoid **split-brain scenario**: consensus via **ZooKeeper** (quorum)
- Avoid Secondary NameNode SPOF via shared edits = **JournalNodes**

## HDFS: High Availability mode

<img src="https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.4/bk_hadoop-high-availability/content/figures/4/figures/bk_system-admin-guide-20140829-image_11.jpeg" alt="HDFS HA" style="zoom:150%;" />

## HDFS HA: Sum up

Components:

- **NameNode**: 1 active NN and 1+ standby NN
- **DataNodes**: store blocks + handles read/write operations
- **JournalNodes**: keep track of every action and build the FSImage

## What is YARN?

Yet Another Resource Negotiator:

- Cluster resource manager:

- - Handles the **RAM** and the **CPU** of workers
  - Allocates resources to applications

- Job monitoring

## YARN: Architecture

- **ResourceManager** (= master):

  - Schedule applications based on available resources
  - Gather information about running applications

- **NodeManager** (= worker): Handle resources on one worker

## YARN: Applications

Application = single job or DAG of jobs

Components (JVMs) of an application:

- **ApplicationMaster**: First container to be allocated, it requests resources for other containers and monitor

- **Containers**: They do the computing

## YARN: Application lifecycle

![YARN app](https://hadoop.apache.org/docs/current2/hadoop-yarn/hadoop-yarn-site/yarn_architecture.gif)

## YARN: Resource sharing

- Queues

  - ECE 70% 100%

  - - APP - 50% 100%
    - INI - 50% 100%

  - Adaltas - 30% 50%

- Fair scheduling

- Solves the peak problem at company level

## Resources

- [HDFS Architecture](https://hadoop.apache.org/docs/r3.1.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [Secondary NameNode - What it really do?](http://blog.madhukaraphatak.com/secondary-namenode---what-it-really-do/)
