# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API operations lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestDirection(str, Enum):
    """
    Direction of the test, which affects how results are shown.
    """

    """
    allowed enum values
    """
    TO_MINUS_TARGET = 'to-target'
    FROM_MINUS_TARGET = 'from-target'
    BIDIRECTIONAL = 'bidirectional'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestDirection from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

