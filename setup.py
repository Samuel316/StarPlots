from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name='starplots',
    version='0.0.1',
    packages=find_packages(),
    author='Samuel Lloyd',
    author_email='samuel.lloyd@ed.ac.uk',
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">3.6",
)
