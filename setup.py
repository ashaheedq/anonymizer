#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='uai-anonymizer',
      version='latest',
      packages=find_packages(exclude=['test', 'test.*']),

      install_requires=[
          'pytest>=3.9.1',
          'flake8>=3.5.0',
          'numpy>=1.20.0',
          'tensorflow>=2.7.0',
          'scipy>=1.7.3',
          'Pillow>=8.3.1',
          'requests>=2.24.0',
          'googledrivedownloader>=0.3',
          'tqdm>=4.28.0',
      ],

      dependency_links=[
      ],
      )
