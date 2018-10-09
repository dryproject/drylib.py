#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Installation script for DRYlib for Python."""

from codecs import open
from os import path
from setuptools import setup, find_packages
from shutil import copyfile

def readfile(*filepath):
  with open(path.join(*filepath), encoding='utf-8') as f:
    return f.read()

PWD = path.abspath(path.dirname(__file__))

VERSION          = readfile(PWD, 'VERSION').rstrip()
LONG_DESCRIPTION = readfile(PWD, 'README.rst')

setup(
  name='drylib',
  version=VERSION,
  description="DRYlib for Python",
  long_description=LONG_DESCRIPTION,
  long_description_content_type='text/x-rst',
  url='https://github.com/dryproject/drylib.py',
  author='Arto Bendiken',
  author_email='arto@dryproject.org',
  license='Public Domain',
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'License :: Public Domain',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Software Development :: Libraries',
    'Topic :: Text Processing :: General',
  ],
  keywords='drylib polyglot',
  project_urls={},
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires=[],
  python_requires='~=3.5',
  extras_require={
    'test': ['pytest'],
  },
)
