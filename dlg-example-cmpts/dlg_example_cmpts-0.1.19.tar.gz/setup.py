"""Python setup.py for dlg_example_cmpts package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("dlg_example_cmpts", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="dlg_example_cmpts",
    version=read("dlg_example_cmpts", "VERSION"),
    description="DALiuGE Component Examples created by ICRAR",
    url="https://github.com/ICRAR/daliuge-component-examples/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="andreas.wicenec@icrar.org",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    extras_require={"test": read_requirements("requirements-test.txt")},
)
