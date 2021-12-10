import uuid

from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')

setup(
    name="pyfg",
    version="0.50",
    packages=find_packages(),
    author="XNET",
    author_email="lindblom+pyfg@spotify.com",
    description="Python API for fortigate",
    url="https://github.com/spotify/pyfg",
    include_package_data=True,
    install_requires=reqs
)
