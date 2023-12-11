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

from monitors_api.models.self_links_links import SelfLinksLinks

class TestSelfLinksLinks(unittest.TestCase):
    """SelfLinksLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SelfLinksLinks:
        """Test SelfLinksLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SelfLinksLinks`
        """
        model = SelfLinksLinks()
        if include_optional:
            return SelfLinksLinks(
                var_self = monitors_api.models.link.Link(
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
            return SelfLinksLinks(
        )
        """

    def testSelfLinksLinks(self):
        """Test SelfLinksLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
