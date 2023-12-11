# coding: utf-8

"""
    Tests API

     ### Overview This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.

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


class Expand(str, Enum):
    """
    Expand
    """

    """
    allowed enum values
    """
    AGENT = 'agent'
    ALERT_MINUS_RULE = 'alert-rule'
    MONITOR = 'monitor'
    LABEL = 'label'
    SHARED_MINUS_WITH_MINUS_ACCOUNT = 'shared-with-account'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Expand from a JSON string"""
        return cls(json.loads(json_str))


