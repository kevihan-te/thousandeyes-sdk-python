# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

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


class EndpointScheduledTestType(str, Enum):
    """
    Type of test being queried.
    """

    """
    allowed enum values
    """
    AGENT_MINUS_TO_MINUS_SERVER = 'agent-to-server'
    HTTP_MINUS_SERVER = 'http-server'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EndpointScheduledTestType from a JSON string"""
        return cls(json.loads(json_str))


