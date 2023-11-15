import pathlib
from setuptools import setup, find_packages

LOCAL_PATH = pathlib.Path(__file__).parent

README = (LOCAL_PATH / "README.md").read_text()

with (LOCAL_PATH / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name='bimage',
    version='0.0.1',
    description='A simple image scraper for use in ML',
    long_description=README,
    author='xobek',
    author_email='garbyow45@gmail.com',
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['bimage=bimage.__main__:main'],
    },
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)