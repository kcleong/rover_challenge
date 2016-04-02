# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='challenge',
    version='0.0.1',
    description='Rover challenge',
    long_description=readme,
    author='Kim Chee Leong',
    author_email='kaceeleong@gmail.com',
    url='https://github.com/kcleong/rover-challenge',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

