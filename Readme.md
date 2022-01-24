## Build and run your data pipeline (pipeline.py) through the DockerFile in this project directory.

"""
docker build -t first_data_pipeline .
docker run -it first_data_pipeline current_date
"""

## Before creating the below postgres docker image, create a directory "ny_taxi_postgres_data" in your current working directory. This diretory will be use to store postgres current state when you create a postgres image using the below command.

"""
docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="password" \
 -e POSTGRES_DB="ny_taxi" \
 -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
 -p 5432:5432 \
 postgres:13

"""

## Open a new terminal, Run "pip install pgcli" to enable you query the postgres database through the terminal.

"""
pip install pgcli
"""
"""
pgcli --help
"""

## Confirm that you have no postgresql running localy first

"""
$ sudo lsof -i :5432
$ kill -9 <PID>
"""

## If the above is right, run "$ sudo pkill -u postgres"

"""
pgcli -h localhost -p 5432 -U root -d ny_taxi
"""

## Use "Control +C" to escape, the you can start running queries

## Download the dataset from

"""
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page#:~:text=January-,Yellow%20Taxi%20Trip%20Records,-(CSV)

"""

## Download the dataset dictionary

"""
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page#:~:text=Yellow%20Trips%20Data%20Dictionary

"""

## Download the taxi_zone look up table

"""
https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page#:~:text=Taxi%20Zone%20Lookup%20Table
"""

## Interfacing with SQL Using Magic Commands

"Magic" commands are special commands that are used to enhance the behaviour of IPython. In order to get our notebook to process SQL within each of our cells, we make use of IPython "magic" commands specifically for SQL. These are provided by the ipython-sql library.

To enable these magic commands, we will give a once-off initialisation command: %load_ext sql

Next, let's discuss the dependencies for each type of SQL database setup.

1. Connecting to a SQL server database
   To connect to a MySQL server database and use our Jupyter notebook as a client application, we first need to install some dependencies. This includes the following Python modules:

Running locally: Once-off installations
pip install psycopg
pip install sqlalchemy
pip install ipython-sql
pip install pymysql
pip install sql_magic
pip install py-postgresql
conda install -c conda-forge pgspecial
Running on Google Colab: For each notebook

pip install pymysql
Assuming, you have a local SQL server installed or have access to credentials to a remote SQL server (e.g. AWS RDS), you can connect to it using a connection string of the following form:

%sql mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}

In practice, you will need to replace the elements of the database url in the connection string with your given credentials, i.e.:

USER - username
PASSWORD - password
HOST - ip address or hostname
PORT - server port number
DATABASE - name of database
We will explore how to connect to a SQL server from a Jupyter notebook in detail in later trains.

2. Connecting to a serverless SQL database
   We can connect to a SQLite database as follows:

We need to install some dependencies. This includes the following Python modules:

Running locally: Once-off installations

pip install sqlalchemy
pip install ipython-sql
pip install pymysql
Running on Google Colab:

no dependencies required
Next, we need a SQLite database file (i.e. with a .db file extension) to connect to. For this purpose, the chinook.db file has been provided, download it from Athena and place it in the same folder as this notebook or some other known location.
After installing the dependencies and downloading the database file, we can now connect to our DB.
