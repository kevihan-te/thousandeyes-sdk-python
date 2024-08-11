# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VisualMode(str, Enum):
    """
    Visual mode in the UI. Either full or half the width of the window.
    """

    """
    allowed enum values
    """
    FULL = 'Full'
    HALF_SCREEN = 'Half screen'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VisualMode from a JSON string"""
        return cls(json.loads(json_str))


