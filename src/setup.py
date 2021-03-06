#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 John Paulett (john -at- 7oars.com)
# Copyright (C) 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import hl7 as _hl7

from distutils.core import setup
    
setup(
    name = 'hl7',
    version = _hl7.__version__,
    description = 'Python library parsing HL7 v2.x and v3.x messages',
    long_description = _hl7.__doc__,
    author = _hl7.__author__,
    author_email = _hl7.__email__,
    url = _hl7.__url__,
    license = _hl7.__license__,
    platforms = ['POSIX', 'Windows'],
    keywords = ['HL7', 'Health Level 7', 'healthcare', 'health care', 'medical record'],
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = ['hl7'],
    test_suite = 'nose.collector',
    zip_safe=False,
)
