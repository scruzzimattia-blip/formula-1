# Beitrage zum F1 Live-Dashboard

Vielen Dank fur dein Interesse, das F1 Live-Dashboard zu verbessern! Wir freuen uns uber jeden Beitrag, ob Bugfix, neues Feature oder Dokumentation.

## 🛠️ Wie kann ich beitragen?

### Fehler melden
- Nutze die GitHub Issues, um Bugs zu beschreiben.
- Gib Details zu deinem Betriebssystem und deiner Docker-Version an.

### Pull Requests (PR)
1. Forke das Repository.
2. Erstelle einen neuen Branch (`git checkout -b feature/neues-feature`).
3. Implementiere deine Änderungen. Achte auf die Einhaltung der Codestruktur.
4. **Wichtig:** Verwende in allen Texten und Kommentaren konsequent "ss" statt "ß".
5. Stelle sicher, dass die Tests (`pytest`) erfolgreich durchlaufen.
6. Erstelle einen Pull Request gegen den `main`-Branch.

## 🧪 Tests ausfuhren

Bevor du einen PR einreichst, teste deine Änderungen lokal:
```bash
pytest
```

## 🏗️ Codestil

- Wir nutzen `flake8` fur das Linting.
- Achte auf aussagekraftige Commit-Nachrichten.
- Halte die `data_provider.py` fur die Logik und `app.py` fur das UI getrennt.

Vielen Dank fur deine Unterstutzung!
