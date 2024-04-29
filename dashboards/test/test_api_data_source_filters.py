# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_data_source_filters import ApiDataSourceFilters

class TestApiDataSourceFilters(unittest.TestCase):
    """ApiDataSourceFilters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDataSourceFilters:
        """Test ApiDataSourceFilters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDataSourceFilters`
        """
        model = ApiDataSourceFilters()
        if include_optional:
            return ApiDataSourceFilters(
                data_source_id = 'VIRTUAL_AGENT',
                filters = [
                    dashboards.models.api_data_source_filter.ApiDataSourceFilter(
                        filter_id = 'TEST_LABEL', 
                        values = ["45862","59749"], 
                        metric_ids = ["WEB_PAGE_LOAD_COMPLETION_RATE","WEB_TTFB","WEB_AVAILABILITY"], )
                    ]
            )
        else:
            return ApiDataSourceFilters(
                data_source_id = 'VIRTUAL_AGENT',
                filters = [
                    dashboards.models.api_data_source_filter.ApiDataSourceFilter(
                        filter_id = 'TEST_LABEL', 
                        values = ["45862","59749"], 
                        metric_ids = ["WEB_PAGE_LOAD_COMPLETION_RATE","WEB_TTFB","WEB_AVAILABILITY"], )
                    ],
        )
        """

    def testApiDataSourceFilters(self):
        """Test ApiDataSourceFilters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
