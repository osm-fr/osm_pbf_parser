#! /usr/bin/env python

from setuptools import setup, find_packages
from setuptools.dist import Distribution
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class BinaryDistribution(Distribution):
    def has_ext_modules(self):
        return True

setup(
    name='osm_pbf_parser',
    version='0.1.1',
    description='OSM PBF Parser binding of libosmpbf',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osm-fr/osm_pbf_parser',
    author='Frederic Rodrigo',
    author_email='fred.rodrigo@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='openstreetmap osm pbf parser libosmpbf',
    packages=find_packages(),
    python_requires='>=2.7, <4',
    platform='manylinux1_x86_64',
    package_data={
        'osm_pbf_parser': ['osm_pbf_parser.so'],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/osm-fr/osm_pbf_parser/issues',
        'Source': 'https://github.com/osm-fr/osm_pbf_parser',
    },
    include_package_data=True,
    distclass=BinaryDistribution,
)
