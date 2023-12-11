# coding: utf-8

"""
    Usage API

    ## Overview These usage endpoints define the following operations: * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the API definitions below for detailed usage instructions and optional parameters.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from usage_api.models.organizations_quotas_assign import OrganizationsQuotasAssign

class TestOrganizationsQuotasAssign(unittest.TestCase):
    """OrganizationsQuotasAssign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationsQuotasAssign:
        """Test OrganizationsQuotasAssign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationsQuotasAssign`
        """
        model = OrganizationsQuotasAssign()
        if include_optional:
            return OrganizationsQuotasAssign(
                organizations = [
                    usage_api.models.organizations_quotas_assign_organizations_inner.OrganizationsQuotasAssign_organizations_inner(
                        org_id = '315', 
                        account_groups = [
                            usage_api.models.account_group_quota.AccountGroupQuota(
                                value = 12000, 
                                aid = '35', )
                            ], )
                    ]
            )
        else:
            return OrganizationsQuotasAssign(
        )
        """

    def testOrganizationsQuotasAssign(self):
        """Test OrganizationsQuotasAssign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
