# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snapshots.models.unexpanded_instant_test_links import UnexpandedInstantTestLinks

class TestUnexpandedInstantTestLinks(unittest.TestCase):
    """UnexpandedInstantTestLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnexpandedInstantTestLinks:
        """Test UnexpandedInstantTestLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnexpandedInstantTestLinks`
        """
        model = UnexpandedInstantTestLinks()
        if include_optional:
            return UnexpandedInstantTestLinks(
                var_self = None,
                test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}]
            )
        else:
            return UnexpandedInstantTestLinks(
        )
        """

    def testUnexpandedInstantTestLinks(self):
        """Test UnexpandedInstantTestLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
