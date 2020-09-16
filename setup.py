#!/usr/bin/env python

from setuptools import setup

REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)

setup(name='Mijn Simpel Client',
      version='1.0',
      description='Python Client to Mijn Simpel',
      author='Aleksandr Vinokurov',
      author_email="aleksandr.vin@gmail.com",
      url='https://github.com/aleksandr-vin/mijn-simpel-python-client',
      packages=['mijn_simpel'],
      install_requires=REQUIRES,
      entry_points = {
        'console_scripts': ['mijn-simpel=mijn_simpel.cli:main'],
      }
     )
