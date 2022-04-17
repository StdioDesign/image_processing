from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="password_generator",
    version="0.0.1",
    author="Darlan Nascimento",
    author_email="darlan.nascimento16@gmail.com",
    description="Testing my first package with DIO Bootcamp",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StdioDesign/password_generator",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    )
