

import pandas as pd
from sqlalchemy import create_engine
from time import time


df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

df.head()

# Check datatype and other vital properties of each columns
df.info()

# Convert the tpep_pickup_datetime & tpep_dropoff_datetime to datetime data type
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.info()

# Generate a DDL statement for schema
print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))

# Creates an postgresql engine using create_engine from sqlAlchemy
pst_sql_engine = create_engine(
    'postgresql://root:Emmanuel1@localhost:5432/ny_taxi')

# Conects engine to database
pst_sql_engine.connect()

# Connect the schema to the connection created above.
# Pandas will execute the result when it tries to create the table
print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=pst_sql_engine))

# To read/write/store a large data set, you carry out the operation in chunks
# Using the iterator and chunksize arguments.
df_in_chunk = pd.read_csv('yellow_tripdata_2021-01.csv',
                          iterator=True, chunksize=100000)
print(df_in_chunk)

df = next(df_in_chunk)
len(df)

# Convert the tpep_pickup_datetime & tpep_dropoff_datetime to datetime data type
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

# Create a table in the database and insert the columns name of the table only
df.head(n=0).to_sql(name="yellow_taxi_data",
                    con=pst_sql_engine, if_exists="replace")

# Load all data in chunks
while True:
    start_time = time()
    df = next(df_in_chunk)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name="yellow_taxi_data", con=pst_sql_engine, if_exists="append")

    stop_time = time()

    print('inserted another chunk, and it took %.3f seconds' %
          (stop_time - start_time))
