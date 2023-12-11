# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from labels_api.models.link import Link

class TestLink(unittest.TestCase):
    """Link unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Link:
        """Test Link
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Link`
        """
        model = Link()
        if include_optional:
            return Link(
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
            return Link(
                href = 'https://api.thousandeyes.com/v7/link/to/resource/id',
        )
        """

    def testLink(self):
        """Test Link"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
