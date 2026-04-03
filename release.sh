#!/bin/bash

# Skript zum Erstellen einer neuen Version (Release)
# Nutzung: ./release.sh [v1.0.0]

VERSION=$1

if [ -z "$VERSION" ]; then
    # Hole den letzten Tag und erhoehe die Minor-Version
    LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v1.0.0")
    BASE=$(echo $LAST_TAG | cut -d. -f1-2)
    PATCH=$(echo $LAST_TAG | cut -d. -f3)
    NEW_PATCH=$((PATCH + 1))
    VERSION="${BASE}.${NEW_PATCH}"
    echo "Keine Version angegeben. Nutze automatische Erhoehung: $VERSION"
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
