from setuptools import setup, find_packages

with open("README.md","r") as infile:
    README = infile.read()

# This call to setup() does all the work
setup(
    name="daraja-py",
    version="1.0.0",
    description="Lipa na mpesa library",
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kamauvick/daraja-py",
    download_url='https://github.com/kamauvick/daraja-py.git',
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
