# coding: utf-8

"""
    Endpoint Tests API

     ## Overview Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API.

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


class SpecificAgentsSelectorType(str, Enum):
    """
    SpecificAgentsSelectorType
    """

    """
    allowed enum values
    """
    SPECIFIC_MINUS_AGENTS = 'specific-agents'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SpecificAgentsSelectorType from a JSON string"""
        return cls(json.loads(json_str))


