#!/bin/bash
conda install pytest pyflakes pip pep8 coverage
pip install pytest-pep8 pytest-cov pytest-flakes bottle==0.12.9 sqlalchemy https://github.com/eblade/sqlalchemy-mtt/archive/master.zip
