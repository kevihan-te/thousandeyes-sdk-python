# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Expand(str, Enum):
    """
    Expand
    """

    """
    allowed enum values
    """
    FILTERS = 'filters'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Expand from a JSON string"""
        return cls(json.loads(json_str))


