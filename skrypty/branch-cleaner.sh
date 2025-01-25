#!/bin/bash
echo "Usuwanie zmerge'owanych gałęzi..."
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
echo "Wszystkie zmerge'owane gałęzie zostały usunięte."
