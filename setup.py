#!/usr/bin/env python

from distutils.core import setup

setup(name='exif2kmz',
      version='0.1',
      description='Converts EXIF geotagged images to KMZ',
      author='Alexander W Blocker',
      author_email='ablocker (at) gmail (dot) com',
      scripts=['scripts/exif2kmz'],
      requires=['Image (>=1.5)','pyexiv2 (>=0.1)']
     )
