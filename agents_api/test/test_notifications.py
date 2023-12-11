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

from agents_api.models.notifications import Notifications

class TestNotifications(unittest.TestCase):
    """Notifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Notifications:
        """Test Notifications
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Notifications`
        """
        model = Notifications()
        if include_optional:
            return Notifications(
                notifications = agents_api.models.notification.Notification(
                    email = agents_api.models.alert_email.AlertEmail(
                        message = 'This test is failing, check as soon as possible.', 
                        recipients = ["user1@thousandeyes.com","user2@cisco.com"], ), 
                    third_party = [
                        agents_api.models.alert_integration_base.AlertIntegrationBase(
                            integration_id = 'wb-78', 
                            integration_name = 'integrationSlack1', 
                            integration_type = 'slack', 
                            target = 'https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ', 
                            auth_method = 'Basic', 
                            auth_user = 'user123', 
                            auth_token = '0VqDYEpidpHVAK397x8PBsmZ', 
                            channel = '#slackChannel', )
                        ], 
                    webhook = [
                        agents_api.models.alert_integration_base.AlertIntegrationBase(
                            integration_id = 'wb-78', 
                            integration_name = 'integrationSlack1', 
                            target = 'https://hooks.slack.com/services/asd/0VqDYEpidpHVAK397x8PBsmZ', 
                            auth_method = 'Basic', 
                            auth_user = 'user123', 
                            auth_token = '0VqDYEpidpHVAK397x8PBsmZ', 
                            channel = '#slackChannel', )
                        ], )
            )
        else:
            return Notifications(
        )
        """

    def testNotifications(self):
        """Test Notifications"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
