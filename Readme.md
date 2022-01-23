## Before creating the below postgres docker image, create a directory "ny_taxi_postgres_data" in your current working directory. This diretory will be use to store postgres current state when you create a postgres image using the below command.

"""
docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="Magadonpay@86" \
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
"""

## If the above is right, run "$ sudo pkill -u postgres"

"""
pgcli -h localhost -p 5432 -U root -d ny_taxi
"""

## Use "Control +C" to escape, the you can start running queries
