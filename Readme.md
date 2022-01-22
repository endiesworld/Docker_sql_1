## Before creating the below docker image, create a directory "ny_taxi_postgres_data" in your current working directory. This diretory will be use to store postgres current state when you create a postgres image using the below command.

"""
docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="Magadonpay@86" \
 -e POSTGRES_DB="ny_taxi" \
 -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
 -p 5432:5432 \
 postgres:13

"""
