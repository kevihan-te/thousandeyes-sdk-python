# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.legacy_default_timespan import LegacyDefaultTimespan

class TestLegacyDefaultTimespan(unittest.TestCase):
    """LegacyDefaultTimespan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LegacyDefaultTimespan:
        """Test LegacyDefaultTimespan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LegacyDefaultTimespan`
        """
        model = LegacyDefaultTimespan()
        if include_optional:
            return LegacyDefaultTimespan(
                timespan_duration = 7200,
                timespan_start = '2023-05-16 10:14:28',
                timespan_end = '2023-05-16 11:14:28'
            )
        else:
            return LegacyDefaultTimespan(
        )
        """

    def testLegacyDefaultTimespan(self):
        """Test LegacyDefaultTimespan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
