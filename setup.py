from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '0.0.2'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]


setup(
    name='sklearn-extensions',
    version=VERSION,
    description='A bundle of 3rd party extensions to scikit-learn',
    long_description=long_description,
    url='https://github.com/wdm0006/sklearn-extensions',
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='scikit-learn sklearn extensions machine learning',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Will McGinnis',
    install_requires=install_requires,
    depedency_links=dependency_links,
    author_email='will@pedalwrencher.com'
)