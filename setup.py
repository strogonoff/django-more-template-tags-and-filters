#coding: utf-8

from distutils.core import setup


setup(
    name='django-more-template-tags-and-filters',
    version='0.1dev',
    packages=['more_template_tags'],
    requires=['python (>= 2.6)',
        'django (>= 1.0)',
        'ttag',
        ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
)
