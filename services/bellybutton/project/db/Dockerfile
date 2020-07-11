# base image
FROM postgres:11.2-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
ADD otu_reference.csv /docker-entrypoint-initdb.d
ADD subjects.csv /docker-entrypoint-initdb.d
ADD test_data.csv /docker-entrypoint-initdb.d
