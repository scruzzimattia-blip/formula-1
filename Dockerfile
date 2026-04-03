# Nutze ein schlankes Python-Image
FROM python:3.9-slim

# Verhindere das Puffern der Ausgabe (Logs sofort sichtbar)
ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Systemabhangigkeiten installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Abhangigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode kopieren
COPY . .

# Port fur Streamlit (Standard 8501)
EXPOSE 8501

# Startbefehl fur das F1-Dashboard
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
