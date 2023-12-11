# coding: utf-8

"""
    Tests API

     ### Overview This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tests_api.models.test_request import TestRequest

class TestTestRequest(unittest.TestCase):
    """TestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestRequest:
        """Test TestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestRequest`
        """
        model = TestRequest()
        if include_optional:
            return TestRequest(
                labels = [9842, 1283],
                shared_with_accounts = [2087, 100],
                alert_rules = [344753, 212697],
                agents = [
                    {"agentId":"125","sourceIpAddress":"1.1.1.1"}
                    ]
            )
        else:
            return TestRequest(
        )
        """

    def testTestRequest(self):
        """Test TestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
