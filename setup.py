from setuptools import setup, find_packages

setup(
    name = 'subdicts',
    version = '0.1',
    url = 'http://github.com/arnellebalane/subdicts',
    license = 'MIT',
    description = 'parses nested dictionay keys into sub-dictionaries',
    author = 'Arnelle Balane',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools']
)
