FROM mysql:5.7
ENV MYSQL_DATABASE=project \
    MYSQL_ROOT_PASSWORD=root
ADD init.sql /docker-entrypoint-initdb.d
EXPOSE 3306