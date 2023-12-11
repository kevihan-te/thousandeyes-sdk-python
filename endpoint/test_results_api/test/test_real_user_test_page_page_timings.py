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

from test_results_api.models.real_user_test_page_page_timings import RealUserTestPagePageTimings

class TestRealUserTestPagePageTimings(unittest.TestCase):
    """RealUserTestPagePageTimings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RealUserTestPagePageTimings:
        """Test RealUserTestPagePageTimings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RealUserTestPagePageTimings`
        """
        model = RealUserTestPagePageTimings()
        if include_optional:
            return RealUserTestPagePageTimings(
                on_content_load = 1483,
                on_load = 4569
            )
        else:
            return RealUserTestPagePageTimings(
        )
        """

    def testRealUserTestPagePageTimings(self):
        """Test RealUserTestPagePageTimings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
