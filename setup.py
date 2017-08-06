#!/usr/bin/python3
# xloverlay_py/setup.py

""" Setuptools project configuration for xloverlay_py. """

from os.path import exists
from setuptools import setup

long_desc = None
if exists('README.md'):
    with open('README.md', 'r') as file:
        long_desc = file.read()

setup(name='xloverlay_py',
      version='0.0.4',
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      long_description=long_desc,
      packages=['xloverlay'],
      package_dir={'': 'src'},
      py_modules=[],
      include_package_data=False,
      zip_safe=False,
      scripts=[],
      description='overlay layer for xlattice_py',
      url='https://jddixon.github.io/xloverlay_py',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
