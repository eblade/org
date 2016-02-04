#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, argparse, configparser

from bikeshedding1.datamodel import Item
from samtt import init, Base

parser = argparse.ArgumentParser(usage="create_tables")
parser.add_argument('-c', '--config', default=os.getenv('BS_CONFIG', 'default.ini'),
    help='specify what config file to run on')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config)


db = init(config['Database']['path'])
db.create_all()
