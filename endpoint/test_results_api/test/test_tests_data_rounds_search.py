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

from test_results_api.models.tests_data_rounds_search import TestsDataRoundsSearch

class TestTestsDataRoundsSearch(unittest.TestCase):
    """TestsDataRoundsSearch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestsDataRoundsSearch:
        """Test TestsDataRoundsSearch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestsDataRoundsSearch`
        """
        model = TestsDataRoundsSearch()
        if include_optional:
            return TestsDataRoundsSearch(
                search_sort = [
                    test_results_api.models.tests_data_search_sort.TestsDataSearchSort(
                        sort = 'round-id', 
                        order = 'desc', )
                    ],
                threshold_filter = test_results_api.models.tests_data_threshold_filters.TestsDataThresholdFilters(
                    filters = [
                        test_results_api.models.tests_data_threshold_filter.TestsDataThresholdFilter(
                            name = 'loss', 
                            value = 1.337, 
                            operator = 'gte', )
                        ], 
                    conditional_operator = 'and', ),
                search_filters = test_results_api.models.tests_data_search_filter.TestsDataSearchFilter(
                    agent_id = [
                        '52455b09-ff1b-4849-8194-99026cc890e0'
                        ], )
            )
        else:
            return TestsDataRoundsSearch(
        )
        """

    def testTestsDataRoundsSearch(self):
        """Test TestsDataRoundsSearch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
