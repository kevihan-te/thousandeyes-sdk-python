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

from alerts_api.models.alert_links import AlertLinks

class TestAlertLinks(unittest.TestCase):
    """AlertLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertLinks:
        """Test AlertLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertLinks`
        """
        model = AlertLinks()
        if include_optional:
            return AlertLinks(
                links = alerts_api.models.rule_links__links.RuleLinks__links(
                    rule = alerts_api.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return AlertLinks(
        )
        """

    def testAlertLinks(self):
        """Test AlertLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
