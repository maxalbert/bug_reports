from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

__version__ = "0.1.0"

setup(
    name="dummy_python_module",
    version=__version__,
    description="Dummy Python Module",
    author="Maximilian Albert",
    author_email="maximilian.albert@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Users",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=["mkdocs>=1"],
)
