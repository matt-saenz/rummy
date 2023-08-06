#!/usr/bin/env bash
set -e

black --check --diff *.py
mypy rummy.py utils.py test_rummy.py
python test_rummy.py
