#!/bin/bash

set -euo pipefail

git pull origin master

. ./venv/bin/activate
python3 documentation_parser.py

if git status --porcelain Versions | grep '^??' > /dev/null 2>&1; then
    git add 'Versions/*'
    version=$(git status --porcelain Versions | head -n1 | sed -Ee 's/.+-([0-9.]+)\..+/\1/')
    git commit -m "Add parsed documentation version $version"
    git push origin master
fi
