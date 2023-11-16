FROM mysql:latest

COPY sql-scripts/init.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=passwr

ENV MYSQL_DATABASE=db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=passwr

WORKDIR /docker-entrypoint-initdb.d

# Expose MySQL port
EXPOSE 3306