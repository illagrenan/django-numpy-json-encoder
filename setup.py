#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

from setuptools import setup

setup(
    name='django-numpy-json-encoder',
    version='0.1.3',
    description="""Django JSON encoder with numpy support.""",
    long_description=io.open("README.rst", 'r', encoding="utf-8").read(),
    url='https://github.com/illagrenan/django-numpy-json-encoder',
    license='MIT',
    author='Vasek Dohnal',
    author_email='vaclav.dohnal@gmail.com',
    packages=['django_numpy_json_encoder'],
    install_requires=['django', 'numpy'],
    python_requires='~=3.6',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
