#!/bin/bash

# Pobierz ostatni tag
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0")
echo "Ostatnia wersja: $LAST_TAG"

# Zwiększ wersję patch (ostatnia cyfra)
NEW_TAG=$(echo $LAST_TAG | awk -F. '{printf "v%d.%d.%d", $1, $2, $3+1}')
echo "Nowa wersja: $NEW_TAG"

# wylacz hook pre-push na czas tagowania
export GIT_PARAMS=""
git tag -a "$NEW_TAG" -m "Nowa wersja: $NEW_TAG"
git push origin "$NEW_TAG"
