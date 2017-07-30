"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read()

setup(name='example_repo',
      version=version,
      description='Analyst Layer',
      # The project's main homepage.
      url='https://www.github.com/example_repo',
      author='',
      author_email='',
       # Choose your license
      license='INTUIT::INTERNAL',
      classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: Other/Proprietary License',

        'Programming Language :: Python :: 2.7',
      ],
      keywords='framework scheduler job runner ETL',
      packages=find_packages(exclude=['tests*']),
      # Include non-python files found in each package in the install.
      include_package_data=True,

      package_data={
        # If any package contains *.json files, include them:
        '': ['*.json', '*.sql', '*.sh'],
      },
      install_requires=['etl_logger'],
      tests_require=[],



      # List additional groups of dependencies here (e.g. development
      # dependencies). You can install these using the following syntax,
      # for example:
      # $ pip install -e .[dev,test]
      extras_require={
        'dev': [
            'mock',
            'nose',
            'pylint',
            'coverage',
            'sphinx'
        ],
        'rel': [
            'mock',
            'nose',
            'pylint',
            'coverage',
            'bumpversion',
            'wheel',
            'sphinx',
        ]
      },
      entry_points={
          'console_scripts': [
              'analyst_layer_run_empty_batches=analyst_layer:run_empty_batches',
          ],
      },
)