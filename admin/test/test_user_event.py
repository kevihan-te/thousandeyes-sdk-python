# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from admin.models.user_event import UserEvent

class TestUserEvent(unittest.TestCase):
    """UserEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserEvent:
        """Test UserEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserEvent`
        """
        model = UserEvent()
        if include_optional:
            return UserEvent(
                aid = '1234',
                account_group_name = 'Account A',
                var_date = '2020-07-17T22:00:54Z',
                event = 'Login failed.',
                ip_address = '99.128.0.0/11',
                uid = '245',
                user = 'API Sandbox User (noreply@thousandeyes.com)',
                resources = [
                    admin.models.user_event_all_of_resources_inner.UserEvent_allOf_resources_inner(
                        type = '', 
                        name = '', )
                    ]
            )
        else:
            return UserEvent(
        )
        """

    def testUserEvent(self):
        """Test UserEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
