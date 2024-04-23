# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alerts.models.get_alert_rule_details200_response import GetAlertRuleDetails200Response

class TestGetAlertRuleDetails200Response(unittest.TestCase):
    """GetAlertRuleDetails200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAlertRuleDetails200Response:
        """Test GetAlertRuleDetails200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAlertRuleDetails200Response`
        """
        model = GetAlertRuleDetails200Response()
        if include_optional:
            return GetAlertRuleDetails200Response(
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
                notifications = alerts.models.notification.Notification(
                    email = alerts.models.notification_email.NotificationEmail(
                        recipients = noreply@thousandeyes.com, 
                        message = 'Notification message', ), 
                    third_party = [
                        alerts.models.notification_third_party.NotificationThirdParty(
                            integration_id = sl-101, 
                            integration_type = 'slack', )
                        ], 
                    webhook = [
                        alerts.models.notification_webhook.NotificationWebhook(
                            integration_id = wb-201, )
                        ], ),
                tests = [
                    null
                    ],
                links = alerts.models.self_links__links.SelfLinks__links(
                    self = alerts.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return GetAlertRuleDetails200Response(
                rule_name = 'The End of the Internet',
                expression = '((hops((hopDelay >= 100 ms))))',
                alert_type = 'http-server',
                rounds_violating_out_of = 5,
                rounds_violating_required = 2,
        )
        """

    def testGetAlertRuleDetails200Response(self):
        """Test GetAlertRuleDetails200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
