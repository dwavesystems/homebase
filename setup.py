from setuptools import setup, find_packages
from os.path import abspath, join, dirname, realpath
from homebase import __version__

here = abspath(dirname(realpath(__file__)))


def readme(folder):
    with open(join(folder, 'README.md')) as desc_file:
        return desc_file.read()


setup(
    name='homebase',
    version=__version__,
    description='A platform independent API for paths in which applications can write data.',
    author='D-Wave Systems Inc.',
    author_email='oshklarsky@dwavesys.com',
    long_description=readme(here),
    packages=find_packages(),
    install_requires=[
        'enum34>=1.1.6'
    ],
    license='Apache 2.0',
    url='https://github.com/dwavesystems/dimod',
    download_url='https://github.com/dwavesys/homebase/archive/{}.tar.gz'.format(__version__)
)
