#!/bin/sh

while ! nc -z container-mysqldb 3306 ; do
    echo "###############################################"
    echo "######## Aguardando container-mysqldb #########"
    echo "###############################################"
    sleep 10
done

echo ">>> container-mysqldb iniciado com sucesso!!!"

# Criar e popular tabelas do basnco
alembic upgrade head

# Executar aplicação
python app.py
