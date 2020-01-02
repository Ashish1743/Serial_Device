from setuptools import setup, find_packages
import setuptools
import subprocess

from pip._internal import main as pipmain
import sys
import warnings
import os


if "--pyprof" in sys.argv:
    with open('requirements.txt') as f:
        required_packages = f.read().splitlines()
        pipmain(["install"] + required_packages)
    try:
        sys.argv.remove("--pyprof")
    except:
        pass
else:
    warnings.warn("Option --pyprof not specified. Not installing PyProf dependencies!")


setup(
name="Serial_Device", # Replace with your own username
version="0.0.1",
author="Ashish Sharma",
author_email="ashishbhardwaj023@.com",
description="All Serial Device Interfacing",
long_description="",
long_description_content_type="text/markdown",
url="https://github.com/Ashish1743/Serial-Device",
packages=setuptools.find_packages(),
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3.0",
    "Operating System :: Debian",
],
python_requires='>=3.6',
)
