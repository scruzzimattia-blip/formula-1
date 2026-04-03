# 🏎️ F1 Live-Dashboard

[![F1 Dashboard CI](https://github.com/DEIN_NUTZERNAME/f1-live-dashboard/actions/workflows/deploy.yml/badge.svg)](https://github.com/DEIN_NUTZERNAME/f1-live-dashboard/actions/workflows/deploy.yml)
[![Docker Publish](https://github.com/DEIN_NUTZERNAME/f1-live-dashboard/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/DEIN_NUTZERNAME/f1-live-dashboard/actions/workflows/docker-publish.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ein interaktives Formel 1 Live-Dashboard basierend auf Python, Streamlit und der `fastf1` Bibliothek. Visualisiere Telemetriedaten, Streckenlayouts und Fahrerpositionen in Echtzeit.

![Screenshot Platzhalter](https://via.placeholder.com/800x400?text=F1+Dashboard+Vorschau)

## ✨ Features

- **Interaktive Map:** Echtzeit-Positionen der Fahrer auf dem Streckenlayout.
- **Live-Statistiken:** Rundenzeiten, Teamfarben und aktuelle Session-Ergebnisse.
- **Effizientes Caching:** Schnelles Laden der Daten durch lokalen FastF1-Cache.
- **Docker-Unterstutzung:** Einfache Bereitstellung und konsistente Ausfuhrung.

## 🚀 Schnellstart (Docker)

Die einfachste Methode, das Dashboard zu nutzen, ist uber das vorkompilierte Docker-Image aus der GitHub Container Registry:

1. **Image herunterladen:**
   ```bash
   docker pull ghcr.io/DEIN_NUTZERNAME/f1-live-dashboard:latest
   ```

2. **Container starten:**
   ```bash
   docker run -d -p 8501:8501 --name f1-dashboard ghcr.io/DEIN_NUTZERNAME/f1-live-dashboard:latest
   ```

3. **Dashboard aufrufen:**
   Offne [http://localhost:8501](http://localhost:8501) in deinem Browser.

## 🛠️ Lokale Entwicklung

Wenn du das Projekt lokal erweitern mochtest:

1. **Repository klonen:**
   ```bash
   git clone https://github.com/DEIN_NUTZERNAME/f1-live-dashboard.git
   cd f1-live-dashboard
   ```

2. **Docker Compose nutzen:**
   ```bash
   docker-compose up --build
   ```

## 📦 Versionierung

Neue Versionen werden mit dem `release.sh` Skript erstellt:
```bash
./release.sh v1.1.0
git push origin v1.1.0
```

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei fur Details.

---
*Hinweis: Ersetze 'DEIN_NUTZERNAME' durch deinen tatsachlichen GitHub-Nutzernamen.*
