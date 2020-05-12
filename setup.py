#!/usr/bin/env python3
import os
from setuptools import setup, find_packages
import sys

readme_path = os.path.join(os.path.split(__file__)[0], "readme.md")
with open(readme_path, "r", encoding='utf8') as fh:
    long_description = fh.read()


setup(
    name='func2cui',
    version="0.0.1",
    author="lcy",
    author_email="lichunyang_1@outlook.com",
    description=("package python function, and export as CUI"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lichunown/func2cui",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(),
    data_files=[],

    entry_points={'console_scripts': [
    ]},

    zip_safe=False
)