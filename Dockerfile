FROM python:3.9-slim

WORKDIR /app

# Copiar arquivos necessários
COPY requirements.txt /app/
COPY app.py /app/
COPY .env /app/
COPY img/logo-completa-branco.png /app/

# Atualizar e instalar dependências
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências do Python
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Executar o Streamlit
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
