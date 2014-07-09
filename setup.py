import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__FILE__), filename)).read()

setup(
    name = 'subdicts',
    version = '1.0.0',
    url = 'https://github.com/arnellebalane/subdicts',
    license = 'MIT',
    description = 'A small python utility which parses nested-keys in dictionaries into sub-dictionaries',
    long_description = read('README.md'),
    author = 'Arnelle Balane',
    author_email = 'arnellebalane@gmail.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
    test_suite = 'subdicts',
    classifiers = [
        'Development Status :: 1 - Released',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
