# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='actioncam2youtube',
    version='0.1.0',
    description='Free your action cam SDcard by pushing to YouTube!',
    long_description=readme,
    author='Luca Pierini',
    author_email='luca.pierini.it@gmail.com',
    url='https://github.com/lucapieroo/actioncam2youtube',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
