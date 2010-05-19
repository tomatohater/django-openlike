#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-openlike',
    version='0.1',
    description='Django template tag for easily implementing and extending OpenLike protocol.',
    author='Drew Engelson',
    author_email='drew@engelson.net',
    url='http://github.com/tomatohater/django-openlike',
    license='New BSD License',
    classifiers=[
      'Framework :: Django',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python',
    ],
    packages=find_packages(),
    zip_safe=False,
)


