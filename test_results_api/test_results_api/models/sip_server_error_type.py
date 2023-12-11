# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SipServerErrorType(str, Enum):
    """
    Error type, none if there is no error
    """

    """
    allowed enum values
    """
    NONE = 'none'
    DNS = 'dns'
    CONNECT = 'connect'
    REGISTER = 'register'
    INVITE = 'invite'
    OPTION = 'option'
    SERVER = 'server'
    SSL = 'ssl'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SipServerErrorType from a JSON string"""
        return cls(json.loads(json_str))


