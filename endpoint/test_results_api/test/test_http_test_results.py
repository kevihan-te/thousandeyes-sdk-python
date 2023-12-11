# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from test_results_api.models.http_test_results import HttpTestResults

class TestHttpTestResults(unittest.TestCase):
    """HttpTestResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpTestResults:
        """Test HttpTestResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpTestResults`
        """
        model = HttpTestResults()
        if include_optional:
            return HttpTestResults(
                results = [
                    null
                    ],
                test = None
            )
        else:
            return HttpTestResults(
        )
        """

    def testHttpTestResults(self):
        """Test HttpTestResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
