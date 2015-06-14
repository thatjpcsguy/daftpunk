#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'requests',
    'colour',
    'flask',
    'argparse'
]

setup(
    name='daftpunk',
    version='1.0',
    description='Phillips Hue SDK',
    author='James Peter Cooper-Stanbury',
    author_email='james@cooperstanbury.com',
    url='https://github.com/thatjpcsguy/daftpunk',
    entry_points={
        'console_scripts': [
            'daftpunk-api = daftpunk.api:main',
            'daftpunk = daftpunk.interpreter:main',
        ]
    },
    requirements=requirements,
    packages=find_packages()
)
