# coding: utf-8

"""
    Alerts API

     ## Overview Manage all alerts, alert rules and alert suppression windows.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from alerts_api.models.alert_metric_detail import AlertMetricDetail

class TestAlertMetricDetail(unittest.TestCase):
    """AlertMetricDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertMetricDetail:
        """Test AlertMetricDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertMetricDetail`
        """
        model = AlertMetricDetail()
        if include_optional:
            return AlertMetricDetail(
                end = None,
                id = '3379',
                name = 'Bucharest, Romania',
                start = None,
                state = 'active',
                type = 'cea_agent'
            )
        else:
            return AlertMetricDetail(
        )
        """

    def testAlertMetricDetail(self):
        """Test AlertMetricDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
