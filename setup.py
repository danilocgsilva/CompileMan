from setuptools import setup

VERSION = "1.0.2"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="CompileMan",
    version=VERSION,
    description="Compiles and clean compileds",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="compilation php node javascript composer",
    url="https://github.com/danilocgsilva/CompileMan",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["compileman"],
    entry_points={"console_scripts": ["cman=compileman.__main__:cman"],},
    include_package_data=True
)

