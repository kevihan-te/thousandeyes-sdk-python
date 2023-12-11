# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dashboards_api.models.api_graphlet_point import ApiGraphletPoint

class TestApiGraphletPoint(unittest.TestCase):
    """ApiGraphletPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiGraphletPoint:
        """Test ApiGraphletPoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiGraphletPoint`
        """
        model = ApiGraphletPoint()
        if include_optional:
            return ApiGraphletPoint(
                x = 1580403900,
                y = 128.249
            )
        else:
            return ApiGraphletPoint(
        )
        """

    def testApiGraphletPoint(self):
        """Test ApiGraphletPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
