#!/bin/bash -e
# Usage
#   $ ./scripts/run_tests.sh
# or
#   $ ./scripts/run_tests.sh --cov pycvodes --cov-report html
python3.5 -m pytest --doctest-modules --pep8 --flakes $@
python3.5 -m doctest README.rst
