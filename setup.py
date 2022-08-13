from setuptools import setup, find_packages

NAME = "my_pdf_tools"
VERSION = "2022.8.12"
DESCRIPTION = ""
long_description = ""
AUTHOR = ""
AUTHOR_EMAIL = ""''""
URL = ""''""
LICENSE = "GPL-3.0 license"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description="",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,

    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,

    install_requires=[
        # 'pandas',
        # 'mysqlclient',
        # 'SQLAlchemy',
    ],

    scripts=[],
    zip_safe=False,
)
