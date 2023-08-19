"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import os
import sys

from setuptools import setup, find_packages

# pylint: disable=redefined-builtin

setup(
    name="ar-tablica-mnozenja",
    # Don't forget to update the version in __init__.py and CHANGELOG.rst!
    version="0.0.1",
    description="Learn multiplication table with arm movements.",
    url="https://github.com/mristin/ar-tablica-mnozenja",
    author="Marko Ristin",
    author_email="marko@ristin.ch",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="License :: OSI Approved :: MIT License",
    keywords="body pose estimation augmented reality learn multiplication table",
    install_requires=[
        "opencv-python>=4,<5",
        "tensorflow==2.12.0",
        "icontract>=2.6.1,<3",
        "tensorflow-hub==0.14.0",
    ],
    extras_require={
        "dev": [
            "black==23.3.0",
            "mypy==1.2.0",
            "pylint==2.17.2",
            "coverage>=6.5.0,<7",
            "pyinstaller>=5,<6",
        ],
    },
    py_modules=["elvolantevirtual"],
    packages=find_packages(exclude=["tests", "continuous_integration", "dev_scripts"]),
    package_data={
        "elvolantevirtual": [
            "media/models/*",
        ]
    },
    entry_points={
        "console_scripts": [
            "ar-tablica-mnozenja=elvolantevirtual.main:entry_point",
        ]
    },
)
