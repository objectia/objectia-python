# objectia-python 
[![Build Status](https://travis-ci.org/objectia/objectia-python.svg?branch=master)](https://travis-ci.org/objectia/objectia-python)
[![codecov](https://codecov.io/gh/objectia/objectia-python/branch/master/graph/badge.svg)](https://codecov.io/gh/objectia/objectia-python)
[![Python](https://img.shields.io/pypi/pyversions/setuptools.svg)]()

Python client for Objectia API

## Documentation

See the [Python API docs](https://docs.objectia.com/guide/python.html).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

    pip install --upgrade objectia

or

    easy_install --upgrade objectia

Install from source with:

    python setup.py install

### Requirements

* Python 2.7 or Python 3.4+

## Usage

The library needs to be configured with your account's API key. Get your own API key by signing up for a free [Objectia account](https://objectia.com).

``` python
import objectia

client = objectia.Client(api_key="YOUR-API-KEY")
location = client.geoip.get("8.8.8.8")
print("Country code: {0}".format(location["country_code"]))
```
