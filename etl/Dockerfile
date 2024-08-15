# Use uma imagem oficial do Python como base
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /etl

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie os scripts ETL para o diretório de trabalho
COPY . .

# Exponha a porta se necessário (normalmente ETL não expõe porta)
# EXPOSE 8000  # Caso necessário

# Comando para rodar o script ETL principal
CMD ["python", "collect_data.py"]
