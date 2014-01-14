from setuptools import setup, find_packages
import sys
import os

version = '0.1'

setup(name='pyfaker',
      version=version,
      description="Create pseudo-random fake data, supports several of languages.",
      long_description="""A libary for generating pseudo-random (but "realistic") data in python. A port of the faker gem to python (making use of its rich locale support).""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='fake language testing data generation',
      author='Andy Hayden',
      author_email='andyhayden1@gmail.com',
      url='https://github.com/hayd/pyfaker',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools'  # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
