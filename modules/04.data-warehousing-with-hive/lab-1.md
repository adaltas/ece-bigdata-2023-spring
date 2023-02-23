# Big Data Ecosystem

## Lab 4.1: Hive Warehouse

### Goals

- Create an external table on top of data stored as CSV
- Create a managed ORC table
- Load data from the CSV table to the ORC table (with some transformations)

### Create an external table

For this lab we will be using a very small dataset of NYC taxi drivers.

Using the official [Hive Data Definition Langage](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL):

1. Using the HDFS CLI, take a look at the data used for this lab at `/education/$GROUP/resources/lab4/nyc_drivers/drivers.csv`

2. Copy the `nyc_drivers` folder to your user directory in HDFS

3. Type `echo $USER` and `echo $GROUP` to retrieve your user and group name

4. Open a Beeline session by typing `beeline`

5. Create an external table targeting our data with the statement below (to be completed). Copy the code to your favourite text editor and finish it. Then, copy the code to the beeline to run it.

   ```sql
   -- REPLACE user AND group WITH YOUR OWN INFORMATION
   SET hivevar:user=YourUserName;
   SET hivevar:group=YourGroupName;
   -- REPLACE hiveUsername, DO NOT USE '.' NOR '-'
   SET hivevar:hiveUsername=l_firstName_school;

   CREATE EXTERNAL TABLE ${group}.${hiveUsername}_nyc_drivers_ext (
     driver_id INT,
     -- COMPLETE THE SCHEMA
   )
   ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
   STORED AS TEXTFILE
   LOCATION -- COMPLETE THE LOCATION
   TBLPROPERTIES ('skip.header.line.count'='1');
   ```

6. Check that the table is correctly created by selecting all the data in it. **If you see only `NULL` values, your schema is not correct.**

### Create a managed ORC table

**Tip:** to create a managed ORC table, you don't have to specify a `LOCATION` nor a `SERDE`:

```sql
CREATE ...
STORED AS ORC;
```

1. Create a managed ORC table (**not external**) that must have the same schema as the external table created above (`${hiveUsername}_nyc_drivers_ext`) but with:
   - The `_ext` prefix removed from the name: `${hiveUsername}_nyc_drivers`
   - The column `name` divided into `first_name` and `last_name` (In this step you only need to define the schema. You will do the split of the column in the next step.)
   - The column `location` renamed as `address` (because `LOCATION` is a Hive keyword)
   - The column `certified` as a `BOOLEAN`
2. Check that your table was created using the HDFS CLI at `/warehouse/tablespace/managed/hive/${GROUP}.db/${hiveUsername}_nyc_drivers` (should be empty)

### Load data from the CSV table to the ORC table

Now we want to populate our ORC table from our CSV table. Using the [Hive Data Manipulation Language](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DML):

1. Write a statement to insert data to the ORC table by applying 2 transformations (check the available [HiveQL string functions](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-StringFunctions)):
   - Split `name` into `first_name` and `last_name`
   - Transform `certified` from `STRING` to `BOOLEAN`
   - Rename `location` to `address`
2. Execute your query
3. Check that the table is correctly created by selecting all the data in it.
4. Check what the data looks like in the managed table using the HDFS CLI at `/warehouse/tablespace/managed/hive/${GROUP}.db/${hiveUsername}_nyc_drivers`