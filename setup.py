# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
from os.path import abspath, join, dirname, realpath

here = abspath(dirname(realpath(__file__)))


def get_version(folder):
    with open(join(folder, 'homebase', '__init__.py')) as init_file:
        regex = """^__version__ = ['"]([^'"]*)['"]"""
        version_match = re.search(regex, init_file.read(), re.M)  # using re.M, ^ is matched to beginning of each line.
        if not version_match:
            raise RuntimeError("Unable to find a version")
        return version_match.group(1)


def readme(folder):
    with open(join(folder, 'README.md')) as desc_file:
        return desc_file.read()


def requirements(folder):
    try:
        with open(join(folder, 'requirements.txt')) as req_file:
            return req_file.readlines()
    except IOError:
        return []


version = get_version(here)

setup(
    name='homebase',
    version=version,
    description='A platform independent API for paths in which applications can write data.',
    author='D-Wave Systems Inc.',
    author_email='oshklarsky@dwavesys.com',
    long_description=readme(here),
    packages=find_packages(),
    install_requires=requirements(here),
    license='Apache 2.0',
    url='https://github.com/dwavesystems/homebase',
    download_url='https://github.com/dwavesystems/homebase/archive/{}.tar.gz'.format(version)
)
