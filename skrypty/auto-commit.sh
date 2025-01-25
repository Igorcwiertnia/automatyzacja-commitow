#!/bin/bash

echo "Automatyczny commit uruchomiony..."

# Dodaj wszystkie zmiany
git add .

# Wykonaj commit z wiadomością
git commit -m "[AUTO] Automatyczny commit" --no-verify

# Opcjonalnie: wyślij zmiany do zdalnego repozytorium
git push
