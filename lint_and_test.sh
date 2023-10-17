#!/usr/bin/env bash
set -e

black --check --diff *.py
isort --check --diff --profile black *.py
mypy --strict *.py
flake8 --extend-ignore E501 *.py
python test_rummy.py
