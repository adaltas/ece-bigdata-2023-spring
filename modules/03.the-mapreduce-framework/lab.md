# Big Data Ecosystem

## Lab 3: The MapReduce Framework

### Goals

- Understand the MapReduce logic
- Run a Python MapReduce job using Hadoop Streaming
- Design a MapReduce job
- Write a Python MapReduce job from scratch

### Run a Python MapReduce word count job using Hadoop Streaming

We will run a MapReduce job that does a word count on text files. It will return the list of words found it the input and the occurence of each one:

```
unclouded       1
uncomfortable   3
uncommonly      6
uncompromised   1
```

1. Clone the repo [ece-bigdata-2022-fall](https://github.com/adaltas/ece-bigdata-2022-fall.git) in your home on the edge node:
   ```bash
   git clone https://github.com/adaltas/ece-bigdata-2022-fall.git
   ```
2. Go to the `modules/03.the-mapreduce-framework/lab-resources/code` directory:
   ```bash
   cd modules/03.the-mapreduce-framework/lab-resources/code
   ```
3. Take a look at the `word_count/mapper.py` and `word_count/reducer.py` files. Tip: open with `vim` for syntax highlighting.
4. Take a look at the input we will use for the MapReduce in HDFS at `/education/ece_2022_fall_bda_1/resources/lab3/mapred-input`
5. The following command will run a MapReduce with 2 reducers, so it will produce 2 output files:
   ```bash
   mapred streaming -D mapreduce.job.reduces=2 \
     -files word_count/mapper.py,word_count/reducer.py \
     -input /education/ece_2022_fall_bda_1/resources/lab3/mapred-input \
     -output /education/ece_2022_fall_bda_1/$USER/lab3/word-count \
     -mapper "python3 mapper.py" -reducer "python3 reducer.py"
   ```
6. Check the output at `/education/ece_2022_fall_bda_1/$USER/lab3/word-count`

### Design a MapReduce job to get the most frequent word

Now, we want to get the **most frequent word** of the input by using the output of our previous `word_count` job.

Design a MapReduce job by defining:

- The output produced by the mapper
- The computation performed by the reducer

**Do not cheat:** You cannot control the number of reduce tasks that will run (their can be more than 1 reduce in 1 reducer container).

### Write the most_frequent MapReduce job

1. Implement the `most_frequent` MapReduce job in Python. Use the `word_count` mapper and reducer as inspiration.
2. Run your job. Specify `-D mapreduce.job.reduces=1` to avoid troubles.
