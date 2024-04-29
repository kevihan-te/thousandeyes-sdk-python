# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from admin.models.get_user_events200_response import GetUserEvents200Response

class TestGetUserEvents200Response(unittest.TestCase):
    """GetUserEvents200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserEvents200Response:
        """Test GetUserEvents200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserEvents200Response`
        """
        model = GetUserEvents200Response()
        if include_optional:
            return GetUserEvents200Response(
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                audit_events = [{accountGroupName=API Sandbox, aid=1234, date=2020-07-17T21:54:54Z, event=Report created., ipAddress=99.128.0.0/11, uid=1234, user=API Sandbox User (noreply@thousandeyes.com), resources=[{name=My New report, type=reportTitle}, {name=Other Report, type=testName}]}, {accountGroupName=API Sandbox, aid=1234, date=2020-07-17T22:00:54Z, event=Login failed., ipAddress=99.128.0.0/11, uid=1234, user=API Sandbox User (noreply@thousandeyes.com)}],
                links = admin.models.pagination_links__links.PaginationLinks__links(
                    previous = admin.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    next = admin.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = , )
            )
        else:
            return GetUserEvents200Response(
        )
        """

    def testGetUserEvents200Response(self):
        """Test GetUserEvents200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
