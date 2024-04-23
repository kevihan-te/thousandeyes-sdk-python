# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestInterval(int, Enum):
    """
    Interval between test runs in seconds.
    """

    """
    allowed enum values
    """
    NUMBER_60 = 60
    NUMBER_120 = 120
    NUMBER_300 = 300
    NUMBER_600 = 600
    NUMBER_900 = 900
    NUMBER_1800 = 1800
    NUMBER_3600 = 3600

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestInterval from a JSON string"""
        return cls(json.loads(json_str))


