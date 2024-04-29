# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.app_links import AppLinks

class TestAppLinks(unittest.TestCase):
    """AppLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppLinks:
        """Test AppLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppLinks`
        """
        model = AppLinks()
        if include_optional:
            return AppLinks(
                links = test_results.models.app_links__links.AppLinks__links(
                    app_link = test_results.models.link.Link(
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
            return AppLinks(
        )
        """

    def testAppLinks(self):
        """Test AppLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
