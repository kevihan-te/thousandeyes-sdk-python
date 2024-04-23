# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.legacy_dashboard_snapshot import LegacyDashboardSnapshot

class TestLegacyDashboardSnapshot(unittest.TestCase):
    """LegacyDashboardSnapshot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegacyDashboardSnapshot:
        """Test LegacyDashboardSnapshot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegacyDashboardSnapshot`
        """
        model = LegacyDashboardSnapshot()
        if include_optional:
            return LegacyDashboardSnapshot(
                account_id = 1234,
                created_date = '2023-05-16 10:14:28',
                expiration_date = '2023-05-16 10:14:28',
                permalink = 'https://app.thousandeyes.com/dashboard/?snapshotId=d28bb71f-5a47-4783-8f12-d4b115e61b0c',
                api_links = [
                    { }
                    ]
            )
        else:
            return LegacyDashboardSnapshot(
        )
        """

    def testLegacyDashboardSnapshot(self):
        """Test LegacyDashboardSnapshot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
