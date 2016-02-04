#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from setuptools import setup


pkg_name = 'org'

ORG_RELEASE_VERSION = os.environ.get(
    'ORG_RELEASE_VERSION', '')  # v*


# http://conda.pydata.org/docs/build.html#environment-variables-set-during-the-build-process
if os.environ.get('CONDA_BUILD', '0') == '1':
    try:
        ORG_RELEASE_VERSION = 'v' + open(
            '__conda_version__.txt', 'rt').readline().rstrip()
    except IOError:
        pass

release_py_path = os.path.join(pkg_name, '_release.py')

if len(ORG_RELEASE_VERSION) > 0:
    if ORG_RELEASE_VERSION[0] == 'v':
        TAGGED_RELEASE = True
        __version__ = ORG_RELEASE_VERSION[1:]
    else:
        raise ValueError("Ill formated version")
else:
    TAGGED_RELEASE = False
    # read __version__ attribute from _release.py:
    exec(open(release_py_path).read())


classifiers = [
    'Development Status :: 3 - Alpha',
    'Operating System :: OS Independent',
]

tests = [
    'org.tests',
]

with open(os.path.join(pkg_name, '__init__.py')) as f:
    long_description = f.read().split('"""')[1]

descr = 'An agile organizer of sorts.'

setup_kwargs = dict(
    name=pkg_name,
    version=__version__,
    description=descr,
    long_description=long_description,
    classifiers=classifiers,
    author='Johan Egneblad',
    author_email='johan.egneblad@DELETEMEgmail.com',
    url='https://github.com/eblade/' + pkg_name,
    license='BSD',
    packages=[pkg_name] + tests,
)

if __name__ == '__main__':
    try:
        if TAGGED_RELEASE:
            # Same commit should generate different sdist
            # depending on tagged version (set $ORG_RELEASE_VERSION)
            # e.g.:  $ ORG_RELEASE_VERSION=v1.2.3 python setup.py
            # sdist this will ensure source distributions contain the correct
            # version
            shutil.move(release_py_path, release_py_path+'__temp__')
            open(release_py_path, 'wt').write(
                "__version__ = '{}'\n".format(__version__))
        setup(**setup_kwargs)
    finally:
        if TAGGED_RELEASE:
            shutil.move(release_py_path+'__temp__', release_py_path)
