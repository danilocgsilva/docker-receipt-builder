from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="docker_receipt_builder",
    version=VERSION,
    description="Automatica creates a docker recepit stack",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="docker receipt",
    url="git@github.com:danilocgsilva/python_setup.git",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["docker_receipt_builder"],
    entry_points={"console_scripts": ["dreceipt=docker_receipt_builder.__main__:main"],},
    include_package_data=True
)

