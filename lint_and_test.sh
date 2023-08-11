#!/usr/bin/env bash
set -e

black --check --diff *.py
mypy --strict rummy.py utils.py
python test_rummy.py
