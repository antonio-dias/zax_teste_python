FROM python:3.11.4-alpine

ENV FLASK_ENV=development

# troca diretório de trabalho
WORKDIR /app

# Copia todos os arquivos para o container
COPY . .

# Instalar o pip e dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt