# Data Engineering with Spark

## Lab 6: Structured Streaming

### Goals

- Stream the NYC Taxi datasets on a socket
- Use Spark Streaming to analyze the stream

### Lab resources

- The `data` directory contains the NYC Taxi datasets;
- The `stream_taxi_data_socket.py` allows to stream a dataset through a socket on a given port.

### Streaming the datasets

To stream the NY datasets:

- Go to this directory:
  ```
  cd ece-spark-2020-fall/labs/lab3
  ```
- Create a checkpoint directory for Spark Streaming in your HDFS personal folder:
  ```bash
  hdfs dfs -mkdir -p "/education/ece/big-data/2020/fall/bda/gr1/$USER/spark-streaming/checkpoint"
  ```
- Run the `stream_taxi_data_socket.py` script. The script has 3 parameters: the server name to use to stream the data, the port on which to open the socket, the dataset to stream (can be either `fares` or `rides`)
  ```bash
  PORT=11111
  hdfs dfs -rm -r -f "/education/ece/big-data/2020/fall/bda/gr1/$USER/spark-streaming/checkpoint/*"
  python3 stream_taxi_data_socket.py edge-1.au.adaltas.cloud "$PORT" fares
  ```
