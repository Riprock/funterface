"""funterface setup script."""

import os

from setuptools import setup


def read(file_name):
    """Read the content of a file adjacent to this script."""
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()

setup(
    name='funterface',
    version='1.0.0',
    author='Fergal Hainey',
    author_email='fergal+funterface@bfot.co.uk',
    description='A fun way to implement class based interfaces.',
    license='Apache-2.0',
    keywords='decorator interface',
    url='https://github.com/Riprock/funterface',
    py_modules=['funterface'],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)
