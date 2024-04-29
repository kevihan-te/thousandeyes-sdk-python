# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agents.models.simple_test_links_self import SimpleTestLinksSelf

class TestSimpleTestLinksSelf(unittest.TestCase):
    """SimpleTestLinksSelf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleTestLinksSelf:
        """Test SimpleTestLinksSelf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleTestLinksSelf`
        """
        model = SimpleTestLinksSelf()
        if include_optional:
            return SimpleTestLinksSelf(
                href = 'https://api.thousandeyes.com/v7/link/to/resource/id',
                templated = True,
                type = '',
                deprecation = '',
                name = '',
                profile = '',
                title = '',
                hreflang = ''
            )
        else:
            return SimpleTestLinksSelf(
                href = 'https://api.thousandeyes.com/v7/link/to/resource/id',
        )
        """

    def testSimpleTestLinksSelf(self):
        """Test SimpleTestLinksSelf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
