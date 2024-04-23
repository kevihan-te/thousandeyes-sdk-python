# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from alerts.models.complete_alert_suppression_window import CompleteAlertSuppressionWindow

class TestCompleteAlertSuppressionWindow(unittest.TestCase):
    """CompleteAlertSuppressionWindow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompleteAlertSuppressionWindow:
        """Test CompleteAlertSuppressionWindow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompleteAlertSuppressionWindow`
        """
        model = CompleteAlertSuppressionWindow()
        if include_optional:
            return CompleteAlertSuppressionWindow(
                alert_suppression_window_id = '2411',
                name = 'Monthly maintenance',
                is_enabled = False,
                status = 'ended',
                start_date = '2017-07-01T05:00Z',
                duration = 0,
                repeat = alerts.models.repeat.Repeat(
                    type = 'week', 
                    interval_type = 'day', 
                    interval_length = 2, 
                    days_of_week = [
                        'sun'
                        ], ),
                end_repeat = alerts.models.end_repeat.EndRepeat(
                    type = 'never', 
                    count = 3, 
                    date = 'Sat Jul 01 01:00:00 BST 2017', ),
                tests = [
                    null
                    ]
            )
        else:
            return CompleteAlertSuppressionWindow(
        )
        """

    def testCompleteAlertSuppressionWindow(self):
        """Test CompleteAlertSuppressionWindow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
