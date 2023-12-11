# coding: utf-8

"""
    Alerts API

     ## Overview Manage all alerts, alert rules and alert suppression windows.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from alerts_api.models.rule_detail_update import RuleDetailUpdate

class TestRuleDetailUpdate(unittest.TestCase):
    """RuleDetailUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleDetailUpdate:
        """Test RuleDetailUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleDetailUpdate`
        """
        model = RuleDetailUpdate()
        if include_optional:
            return RuleDetailUpdate(
                rule_id = '127094',
                rule_name = 'The End of the Internet',
                expression = '((hops((hopDelay >= 100 ms))))',
                direction = 'to-target',
                notify_on_clear = True,
                is_default = True,
                alert_type = 'http-server',
                minimum_sources = 10,
                minimum_sources_pct = 99,
                rounds_violating_mode = 'exact',
                rounds_violating_out_of = 5,
                rounds_violating_required = 2,
                include_covered_prefixes = True,
                severity = 'major',
                notifications = alerts_api.models.notification.Notification(
                    email = alerts_api.models.notification_email.NotificationEmail(
                        recipients = noreply@thousandeyes.com, 
                        message = 'Notification message', ), 
                    third_party = [
                        alerts_api.models.notification_third_party.NotificationThirdParty(
                            integration_id = sl-101, 
                            integration_type = 'slack', )
                        ], 
                    webhook = [
                        alerts_api.models.notification_webhook.NotificationWebhook(
                            integration_id = wb-201, )
                        ], ),
                test_ids = [
                    '["281474976710706","271659"]'
                    ]
            )
        else:
            return RuleDetailUpdate(
                rule_name = 'The End of the Internet',
                expression = '((hops((hopDelay >= 100 ms))))',
                alert_type = 'http-server',
                rounds_violating_out_of = 5,
                rounds_violating_required = 2,
        )
        """

    def testRuleDetailUpdate(self):
        """Test RuleDetailUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
