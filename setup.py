#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'requests',

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
            'daftpunk-api = api.main:main',
            'daftpunk = interpreter.main:main',
        ]
    },
    requirements=requirements,
    packages=find_packages()
)
