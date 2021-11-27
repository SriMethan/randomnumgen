import os
import io
import setuptools

def read_description():
  description = io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()
  return description

setuptools.setup(
    name="randomnumgen",
    version="0.1",
    author="SriMethan",
    description="A Python3 library that generates random numbers.",
    long_description= read_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/SriMethan/randomnumgen",
    project_urls={
        "Bug Tracker": "hhttps://github.com/SriMethan/randomnumgen/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "randomnumgen"},
    packages=setuptools.find_packages(where="randomnumgen"),
    python_requires=">=3",
)
