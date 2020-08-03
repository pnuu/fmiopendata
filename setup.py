#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Panu Lahtinen
#
# Author(s):
#
#   Panu Lahtinen <pnuu+git@iki.fi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Setup for trollflow2."""

from setuptools import setup
from fmiopendata import __version__

install_requires = ['numpy']
extras_require = {'radar': ['rasterio'],
                  'grid': ['eccodes'],
                  }
all_extras = []
for extra_deps in extras_require.values():
    all_extras.extend(extra_deps)
extras_require['all'] = list(set(all_extras))

setup(name="fmiopendata",
      version=__version__,
      description='Python library for accessing FMI open data',
      long_description='Python library for accessing FMI open data',
      author='Panu Lahtinen',
      author_email='pnuu+git@iki.fi',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 " +
                   "or later (GPLv3+)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Scientific/Engineering",
                   ],
      url="https://github.com/pnuu/pyfmiopendata",
      packages=['fmiopendata', ],
      scripts=["bin/wms_html.py",
               "bin/wfs_html.py",
               ],
      data_files=[],
      install_requires=install_requires,
      extras_require=extras_require,
      tests_require=['rasterio', 'eccodes'],
      python_requires='>=3.4',
      )
