#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities for ansible',
      author='Binh Nguyen',
      author_email='',
      url='',
      install_requires=[
      	'boto',
      	'pymongo',
      	'pyyaml',
      	'fluent-logger'
      ],
     )
