# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

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


class DurationUnit(str, Enum):
    """
    Timespan unit.
    """

    """
    allowed enum values
    """
    MINUTE = 'minute'
    HOUR = 'hour'
    DAY = 'day'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DurationUnit from a JSON string"""
        return cls(json.loads(json_str))


