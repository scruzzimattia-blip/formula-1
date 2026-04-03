# --- Stage 1: Build-Umgebung ---
FROM python:3.9-slim AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /build

# Systemabhangigkeiten fur den Build-Prozess
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Abhangigkeiten installieren (in einen lokalen Ordner)
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# --- Stage 2: Laufzeit-Umgebung ---
FROM python:3.9-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/appuser/.local/bin:${PATH}"

WORKDIR /app

# Erstelle einen Non-Root User
RUN groupadd -r appgroup && useradd -r -g appgroup -m appuser
USER appuser

# Kopiere installierte Python-Pakete vom Builder
COPY --from=builder --chown=appuser:appgroup /root/.local /home/appuser/.local

# Kopiere Anwendungscode
COPY --chown=appuser:appgroup . .

# Verzeichnis fur den FastF1-Cache vorbereiten (falls nicht durch Volume gemappt)
RUN mkdir -p /home/appuser/fastf1_cache

# Port fur Streamlit
EXPOSE 8501

# Startbefehl
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
