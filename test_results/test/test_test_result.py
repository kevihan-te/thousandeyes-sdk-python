# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.test_result import TestResult

class TestTestResult(unittest.TestCase):
    """TestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestResult:
        """Test TestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestResult`
        """
        model = TestResult()
        if include_optional:
            return TestResult(
                links = {appLink={href=https://app.thousandeyes.com/view/tests?__a=105&testId=195&roundId=1692916680&agentId=125}},
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800
            )
        else:
            return TestResult(
        )
        """

    def testTestResult(self):
        """Test TestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
