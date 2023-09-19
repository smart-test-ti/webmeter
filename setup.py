#!/usr/bin/env python
# coding: utf-8
#
# Licensed under MIT
#
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    install_requires=['fastapi','uvicorn', 'requests', 'loguru', 'fire','pyfiglet','psutil',
    'pyyaml','python-multipart','sqlalchemy'],
    version='1.0.7',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="WebMeter - A web api-performance tool based on jmeter.",
    packages=setuptools.find_namespace_packages(include=["webmeter", "webmeter.*"], ),
    include_package_data=True
)
