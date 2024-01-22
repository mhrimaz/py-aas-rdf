#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Mohammad Hossein Rimaz",
    author_email='hossein.rimaz@mycompany.de',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="Utility library to de-/serialize AAS in RDF and JSON.",
    entry_points={
        'console_scripts': [
            'py_aas_rdf=py_aas_rdf.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords="py_aas_rdf asset administration shell sdk industry 4.0 industrie i4.0 industry iot iiot",
    name='py_aas_rdf',
    packages=find_packages(include=['py_aas_rdf', 'py_aas_rdf.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mhrimaz/py-aas-rdf',
    version='0.0.1',
    zip_safe=False,
)
