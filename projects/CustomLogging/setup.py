#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='CustomLogging',
    version='0.1',
    author='Puneet Reddy',
    author_email='puneet.reddy@beyondanalysis.net',
    description='A custom handler to send log messages to a postgresql db',
    packages=find_packages(exclude=['tests']),
    long_description=open('README.txt').read(),
    install_requires=[
        'SQLAlchemy==1.2.10',
        'psycopg2==2.7.5'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    zip_safe=True
)