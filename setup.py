#  MIT License
#
#  Copyright (c) 2020 Sam McCormack
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import os
from os.path import dirname, abspath

import setuptools
from setuptools import setup

import pathmod

os.chdir(dirname(abspath(__file__)))

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pathmod",
    version=pathmod.__version__,
    packages=setuptools.find_packages(),
    python_requires="~=3.6",
    description="CLI tool for easily modifying the PATH (persistently) on Windows.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sam McCormack",
    author_email="cabbagedevelopment@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={"Source": "https://github.com/CabbageDevelopment/pathmod"},
    keywords="cli tool path windows",
    entry_points={"console_scripts": ["pathmod=pathmod:cli"]},
)
