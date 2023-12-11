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

from dashboards_api.models.dashboard_snapshot_links_links import DashboardSnapshotLinksLinks

class TestDashboardSnapshotLinksLinks(unittest.TestCase):
    """DashboardSnapshotLinksLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardSnapshotLinksLinks:
        """Test DashboardSnapshotLinksLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardSnapshotLinksLinks`
        """
        model = DashboardSnapshotLinksLinks()
        if include_optional:
            return DashboardSnapshotLinksLinks(
                var_self = dashboards_api.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', ),
                app_link = dashboards_api.models.link.Link(
                    href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                    templated = True, 
                    type = '', 
                    deprecation = '', 
                    name = '', 
                    profile = '', 
                    title = '', 
                    hreflang = '', )
            )
        else:
            return DashboardSnapshotLinksLinks(
        )
        """

    def testDashboardSnapshotLinksLinks(self):
        """Test DashboardSnapshotLinksLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
