# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TestPageLoadingStrategy(str, Enum):
    """
    * `normal`: The test waits until the entire page is fully loaded, including the downloading and parsing of HTML content as well as all associated resources, before advancing to the next action in the transaction test script.  * `eager`: The test waits for the DOMContentLoaded event, indicating that HTML content is downloaded and parsed, and the document reaches the \"interactive\" readiness state, before proceeding to the next action in the test script. * `none`: The test only waits for the download of HTML content. Once the HTML is downloaded, the test continues to the next action in the transaction test script without waiting for additional resources. 
    """

    """
    allowed enum values
    """
    NORMAL = 'normal'
    EAGER = 'eager'
    NONE = 'none'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TestPageLoadingStrategy from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        """Handle unknown values"""
        return cls.UNKNOWN

