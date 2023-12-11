# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agents_api.models.account_group_id import AccountGroupId

class TestAccountGroupId(unittest.TestCase):
    """AccountGroupId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountGroupId:
        """Test AccountGroupId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountGroupId`
        """
        model = AccountGroupId()
        if include_optional:
            return AccountGroupId(
                aid = '11'
            )
        else:
            return AccountGroupId(
        )
        """

    def testAccountGroupId(self):
        """Test AccountGroupId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
