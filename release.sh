#!/bin/bash

# Skript zum Erstellen einer neuen Version (Release)
# Nutzung: ./release.sh v1.0.0

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Fehler: Bitte geben Sie eine Versionsnummer an (z.B. ./release.sh v1.0.0)"
    exit 1
fi

# Uberpruefen, ob das Format stimmt (vX.Y.Z)
if [[ ! $VERSION =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Fehler: Ungultiges Versionsformat. Bitte nutzen Sie vX.Y.Z (z.B. v1.0.0)"
    exit 1
fi

echo "Erstelle Release fur Version: $VERSION"

# Git-Tag lokal erstellen
git tag -a "$VERSION" -m "Release $VERSION"

echo "Tag $VERSION wurde lokal erstellt."
echo "Nutzen Sie 'git push origin $VERSION', um den Tag zu veroffentlichen."
echo "Die GitHub Action wird anschliessend automatisch das Docker-Image bauen und pushen."
