=========================
Django numpy JSON encoder
=========================

.. image:: https://img.shields.io/pypi/v/django-numpy-json-encoder.svg
    :target: https://pypi.python.org/pypi/django-numpy-json-encoder
    :alt: PyPi

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/django-numpy-json-encoder/
    :alt: MIT

.. image:: https://img.shields.io/travis/illagrenan/django-numpy-json-encoder.svg
    :target: https://travis-ci.org/illagrenan/django-numpy-json-encoder
    :alt: TravisCI

.. image:: https://img.shields.io/coveralls/illagrenan/django-numpy-json-encoder.svg
    :target: https://coveralls.io/github/illagrenan/django-numpy-json-encoder?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/pypi/implementation/django-numpy-json-encoder.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python implementations

.. image:: https://img.shields.io/pypi/pyversions/django-numpy-json-encoder.svg
    :target: https://pypi.python.org/pypi/django_brotli/
    :alt: Supported Python versions

Introduction
------------

Subclass of standard Django JSON encoder [1]_ that can encode some numpy types (integers, floats and arrays).

.. [1] https://docs.djangoproject.com/en/dev/topics/serialization/#djangojsonencoder

Installation
------------

- Supported Python versions are:  ``3.6`` and ``3.7-dev``.
- Supported Django versions are: ``2.0``

.. code:: shell

    pip install --upgrade django-numpy-json-encoder

Usage
-----

.. code:: python

    # -*- encoding: utf-8 -*-
    # ! python3

    import numpy as np
    from django.http import JsonResponse
    from django.views import View

    from django_numpy_json_encoder.numpy_encoder import NumpyJSONEncoder


    class ExampleView(View):
        # noinspection PyMethodMayBeStatic
        def post(self, *args, **kwargs):
            numpy_array = np.random.rand(8, 42).astype(np.float32)

            return JsonResponse(data={'array': numpy_array}, encoder=NumpyJSONEncoder, safe=True)

License
-------

The MIT License (MIT)
