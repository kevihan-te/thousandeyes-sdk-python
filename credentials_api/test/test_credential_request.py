# coding: utf-8

"""
    Credentials API

    ### Overview Manage credentials for transaction tests using the Credentials API.   The following permissions are required to access Credentials API endpoints:  * `Settings Tests Read` for read operations.  * `Settings Tests Update` for write operations.  * `View sensitive data in web transaction scripts` to view the encrypted value property of credentials.  * `Settings Tests Create Transaction (Tx) Tests` to create credentials.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from credentials_api.models.credential_request import CredentialRequest

class TestCredentialRequest(unittest.TestCase):
    """CredentialRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialRequest:
        """Test CredentialRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CredentialRequest`
        """
        model = CredentialRequest()
        if include_optional:
            return CredentialRequest(
                name = 'Example Credential 1',
                value = 'Example Credential 1 Password'
            )
        else:
            return CredentialRequest(
        )
        """

    def testCredentialRequest(self):
        """Test CredentialRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
