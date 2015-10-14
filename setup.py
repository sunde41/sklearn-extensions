from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
    install_requires=[
        'numpy>=1.9.0',
        'scikit-learn>=0.15',
        'scipy>=0.16.0',
        'patsy>=0.4',
        'lda>=1.0.2',
        'sklearn-compiledtrees>=1.2'
    ],
    depedency_links=[
        'https://github.com/jmetzen/kernel_regression.git',
        'https://github.com/jmetzen/sparse-filtering.git',
        'https://github.com/all-umass/metric-learn.git',
        'https://github.com/nicodv/kmodes.git',
        'https://github.com/amueller/patsylearn.git',
        'https://github.com/predikto/pyculearn.git'
    ],
    author_email='will@pedalwrencher.com'
)