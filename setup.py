# setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Obsidian Service',
    version='0.0.1',
    description='Obsidian Service that runs in the background to make life easier',
    long_description=readme,
    author='Harry Thang',
    author_email='harry.thang@pm.me',
    url='https://github.com/hazzashirt/obsidian-service',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

