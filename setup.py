import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="lipanampesa",
    version="1.0.0",
    description="Lipa na mpesa library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kamauvick/package_test",
    author="Victor Waichigo",
    author_email="waichigovick@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["requests", "python-decouple"],
)
