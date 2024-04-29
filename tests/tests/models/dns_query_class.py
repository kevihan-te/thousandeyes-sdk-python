# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DnsQueryClass(str, Enum):
    """
    Domain class used by this test. 'in' stands for Internet, while 'ch' stands for Chaos.
    """

    """
    allowed enum values
    """
    IN = 'in'
    CH = 'ch'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DnsQueryClass from a JSON string"""
        return cls(json.loads(json_str))


