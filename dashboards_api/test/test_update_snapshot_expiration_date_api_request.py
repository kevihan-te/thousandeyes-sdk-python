# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dashboards_api.models.update_snapshot_expiration_date_api_request import UpdateSnapshotExpirationDateApiRequest

class TestUpdateSnapshotExpirationDateApiRequest(unittest.TestCase):
    """UpdateSnapshotExpirationDateApiRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSnapshotExpirationDateApiRequest:
        """Test UpdateSnapshotExpirationDateApiRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSnapshotExpirationDateApiRequest`
        """
        model = UpdateSnapshotExpirationDateApiRequest()
        if include_optional:
            return UpdateSnapshotExpirationDateApiRequest(
                snapshot_expiration_date = '2023-05-16T10:14:28Z'
            )
        else:
            return UpdateSnapshotExpirationDateApiRequest(
        )
        """

    def testUpdateSnapshotExpirationDateApiRequest(self):
        """Test UpdateSnapshotExpirationDateApiRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
