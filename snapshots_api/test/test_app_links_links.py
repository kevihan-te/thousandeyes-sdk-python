# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from snapshots_api.models.app_links_links import AppLinksLinks

class TestAppLinksLinks(unittest.TestCase):
    """AppLinksLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppLinksLinks:
        """Test AppLinksLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppLinksLinks`
        """
        model = AppLinksLinks()
        if include_optional:
            return AppLinksLinks(
                app_link = snapshots_api.models.link.Link(
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
            return AppLinksLinks(
        )
        """

    def testAppLinksLinks(self):
        """Test AppLinksLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
