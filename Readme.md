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
