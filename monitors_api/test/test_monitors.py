# coding: utf-8

"""
    BGP Monitors

     ## Overview Retrieve information about BGP monitors available for ThousandEyes account.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from monitors_api.models.monitors import Monitors

class TestMonitors(unittest.TestCase):
    """Monitors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Monitors:
        """Test Monitors
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Monitors`
        """
        model = Monitors()
        if include_optional:
            return Monitors(
                monitors = [
                    monitors_api.models.monitor.Monitor(
                        country_id = 'GB', 
                        monitor_id = '1234', 
                        ip_address = '4.69.184.193', 
                        network = 'Level 3 Communications, Inc. (AS 3356)', 
                        monitor_type = 'public', 
                        monitor_name = 'Seattle, WA', )
                    ]
            )
        else:
            return Monitors(
        )
        """

    def testMonitors(self):
        """Test Monitors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
