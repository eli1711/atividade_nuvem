# Use a imagem oficial do MySQL
FROM mysql:8.0

# Definir variáveis de ambiente para o banco de dados
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=projeto
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

# Copiar o script de inicialização do banco de dados (caso tenha algum script SQL para criar tabelas)
COPY ./db/init.sql /docker-entrypoint-initdb.d/

# Expor a porta 3306 para o MySQL
EXPOSE 3306

# Comando para iniciar o MySQL
CMD ["mysqld"]
