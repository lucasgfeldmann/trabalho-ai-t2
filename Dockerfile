# Imagem base leve oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia e instala as dependências antes para otimizar o cache de build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia os diretórios de código e testes
COPY src/ ./src/
COPY tests/ ./tests/

# Comando padrão: executa o Harness de testes para homologação automática
CMD ["python", "tests/test_harness.py"]
