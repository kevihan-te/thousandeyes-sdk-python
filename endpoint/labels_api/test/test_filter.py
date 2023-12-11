# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from labels_api.models.filter import Filter

class TestFilter(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Filter:
        """Test Filter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Filter`
        """
        model = Filter()
        if include_optional:
            return Filter(
                key = 'vpn-client-network',
                values = ["10.1.1.0/24","192.168.1.0/24"],
                mode = 'in'
            )
        else:
            return Filter(
        )
        """

    def testFilter(self):
        """Test Filter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
