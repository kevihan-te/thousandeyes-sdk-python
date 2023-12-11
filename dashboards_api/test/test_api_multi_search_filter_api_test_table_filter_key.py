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

from dashboards_api.models.api_multi_search_filter_api_test_table_filter_key import ApiMultiSearchFilterApiTestTableFilterKey

class TestApiMultiSearchFilterApiTestTableFilterKey(unittest.TestCase):
    """ApiMultiSearchFilterApiTestTableFilterKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiMultiSearchFilterApiTestTableFilterKey:
        """Test ApiMultiSearchFilterApiTestTableFilterKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiMultiSearchFilterApiTestTableFilterKey`
        """
        model = ApiMultiSearchFilterApiTestTableFilterKey()
        if include_optional:
            return ApiMultiSearchFilterApiTestTableFilterKey(
                key = 'Target',
                value = ''
            )
        else:
            return ApiMultiSearchFilterApiTestTableFilterKey(
        )
        """

    def testApiMultiSearchFilterApiTestTableFilterKey(self):
        """Test ApiMultiSearchFilterApiTestTableFilterKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
