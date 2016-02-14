#!/usr/bin/env python3

from samtt import init

db = init('sqlite:////tmp/test.sqlite')
db.create_all()
