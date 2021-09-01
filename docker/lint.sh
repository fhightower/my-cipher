#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort cipher.py tests/

black cipher.py tests/

mypy cipher.py tests/

pylint --fail-under 9 cipher.py

flake8 cipher.py
