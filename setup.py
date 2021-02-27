#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
import os

from setuptools import setup


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def get_install_requirements(path):
    content = read(path)
    return [req for req in content.split("\n") if req != "" and not req.startswith("#")]


# From https://github.com/jupyterlab/jupyterlab/blob/master/setupbase.py, BSD licensed
def find_packages():
    here = os.path.abspath(os.path.dirname(__file__))
    packages = []
    for d, dirs, _ in os.walk(here, followlinks=True):
        if os.path.exists(os.path.join(d, "__init__.py")):
            packages.append(os.path.relpath(d, here).replace(os.path.sep, "."))
        elif d != here:
            # Do not look for packages in subfolders if current is not a package
            dirs[:] = []
    return packages


URL = "https://github.com/baogianghoangvu/pandas-shortcuts"

setup(
    name="pandas_shortcuts",
    version="0.0.1",
    description="Why even wait for autocompletion when you can use `pandas_shortcuts`?",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="BaoGiang HoangVu",
    author_email="hoangvubaogiang@gmail.com",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_install_requirements("requirements.txt"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": f"{URL}/issues",
        "Source": URL,
    },
)
