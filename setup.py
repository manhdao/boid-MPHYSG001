from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "1.0",
    author = "Manh Dao (Marvin)",
    author_email = "ducmanhdao92@gmail.com",
    description = ("An implementation of the boids system with 3 movement defining functions"),
    long_description = open('README.md', 'r').read(),
    license = "MIT",
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse','numpy','yaml','simulate','matplotlib']
)

