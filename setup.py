# Copyright (c) 2014, Facebook, Inc.  All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
from setuptools import setup, find_packages

NAME = 'varint'
VERSION = '1.0.2'

setup(
    name=NAME,
    version=VERSION,
    py_modules=['varint'],
    description="Simple python varint implementation",

    author='Peter Ruibal',
    author_email='ruibalp@gmail.com',
    license='MIT',
    keywords='encoder',
    url='http://github.com/fmoo/python-varint',
    download_url='https://github.com/fmoo/python-varint/%s.tar.gz' % VERSION,

    #test_suite="tests",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
