from setuptools import setup, find_packages
from os.path import abspath, join, dirname, realpath
from tracts import __version__

here = abspath(dirname(realpath(__file__)))


def readme(folder):
    with open(join(folder, 'README.md')) as desc_file:
        return desc_file.read()


setup(
    name='tracts',
    version=__version__,
    description='A platform independent API for paths in which applications can write data.',
    author='D-Wave Systems Inc.',
    author_email='oshklarsky@dwavesys.com',
    long_description=readme(here),
    packages=find_packages(),
)
