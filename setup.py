# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='epc_data_downloader',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Khalim Conn-Kowlessar',
    author_email='kconnnkowlessar@gmail.com',
    url='https://github.com/KhalimCK/epc-data-exploration.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
