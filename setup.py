#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:
#
# Copyright 2013-2014 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.core import setup
from setuptools import setup, find_packages
from distutils.command.build import build as _build
import firenado

import os, sys
import subprocess


install_requires = [
    "tornado>=4.1",
    "redis>=2.9.1",
    "sqlalchemy==0.9.4",
]

setup(
    name='Firenado',
    version=firenado.__version__,
    description='Componentized web framework.',
    license='Apache License V2.0',
    author='Flavio Garcia',
    author_email='piraz@candango.org',
    url='http://www.firenado.io/',
    packages=[
        'firenado',
        'firenado.core',
        'firenado.core.management',
        'firenado.util',
    ],
    package_dir={'firenado': 'firenado'},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    scripts=['firenado/bin/firenado-cli.py'],
    entry_points={'console_scripts': [
        'firenado = firenado.core.management:run_from_command_line',
    ]},
)
