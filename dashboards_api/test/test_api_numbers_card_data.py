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

from dashboards_api.models.api_numbers_card_data import ApiNumbersCardData

class TestApiNumbersCardData(unittest.TestCase):
    """ApiNumbersCardData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiNumbersCardData:
        """Test ApiNumbersCardData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiNumbersCardData`
        """
        model = ApiNumbersCardData()
        if include_optional:
            return ApiNumbersCardData(
                card_id = 'lrxxr',
                start_date = '2023-05-16T10:14:28Z',
                end_date = '2023-05-16T10:14:28Z',
                previous_value = 500.0,
                bin_size = 3600,
                timestamp = 1567620000,
                number_of_data_points = 24192,
                value = 100.0,
                status = 'No data',
                alert_suppression_windows = [
                    dashboards_api.models.api_dashboard_asw.ApiDashboardAsw(
                        id = '281474976710662', 
                        name = 'Test dashboards', 
                        test_ids = ["281474976710661"], 
                        start_times = ["2023-05-16T10:14:28Z"], 
                        duration_in_seconds = 7200, 
                        repeat = 'custom', 
                        repeat_every = 5, 
                        repeat_unit = 'week', )
                    ]
            )
        else:
            return ApiNumbersCardData(
        )
        """

    def testApiNumbersCardData(self):
        """Test ApiNumbersCardData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
