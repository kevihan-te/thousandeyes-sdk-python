# coding: utf-8

"""
    Instant Tests API

     ### Overview The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests_api.api.dns_trace_api import DNSTraceApi


class TestDNSTraceApi(unittest.TestCase):
    """DNSTraceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DNSTraceApi()

    def tearDown(self) -> None:
        pass

    def test_post_instant_dns_trace(self) -> None:
        """Test case for post_instant_dns_trace

        Create DNS trace instant test
        """
        pass


if __name__ == '__main__':
    unittest.main()
