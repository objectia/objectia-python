import os
import sys
from setuptools import setup

# to install objectia type the following command:
#      python setup.py install

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

with open("DESCRIPTION.rst") as f:
    long_description = f.read()

version_contents = {}
with open(os.path.join('objectia', 'version.py')) as f:
    exec(f.read(), version_contents)

setup(
    name="objectia",
    version=version_contents['VERSION'],
    description="Python client for Objectia API",
    long_description=long_description,
    author="Objectia",
    author_email="hello@objectia.com",
    url="http://github.com/objectia/objectia-python",
    license="MIT",
    keywords=["objectia", "api", "geoip", "geolocation"],
    install_requires=[
        "requests>=2.5.0",
        "PyJWT>=1.6.1"
    ],
    packages=["objectia"],
    test_suite="tests",
    classifiers=[
        #  "Development Status :: 5 - Production/Stable",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
