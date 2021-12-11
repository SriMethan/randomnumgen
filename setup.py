import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="randomnumgen",
    version="1.1.0",
    author="SriMethan",
    description="A Python3 library that generates random numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SriMethan/randomnumgen",
    project_urls={
        "Bug Tracker": "https://github.com/SriMethan/randomnumgen/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
