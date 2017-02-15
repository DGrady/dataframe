# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dataframe',
    version='0.1.0',
    description='A simple API for Pandas data frames',
    long_description=readme,
    author='Daniel Grady',
    author_email='danielgrady@danielgrady.info',
    url='https://github.com/DGrady/dataframe',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
