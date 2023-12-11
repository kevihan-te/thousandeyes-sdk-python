# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "labels-api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Labels API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/thousandeyes/thousandeyes-python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "Labels API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    ### Overview This is API for the Labels API (formerly called groups).
    """,  # noqa: E501
    package_data={"labels_api": ["py.typed"]},
)
