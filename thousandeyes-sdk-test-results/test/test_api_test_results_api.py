# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.api_test_results_api import APITestResultsApi


class TestAPITestResultsApi(unittest.TestCase):
    """APITestResultsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = APITestResultsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_api_agent_round_results_models_validation(self) -> None:
        """Test case for get_test_api_agent_round_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "completion" : 100.0,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "errorType" : "None",
                    "apiTransactionTime" : 990.1,
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "requests" : [ {
                      "completion" : 100.0,
                      "stepType" : "default",
                      "responseTime" : 440.8,
                      "apiCallTime" : 900.9,
                      "processingTime" : 59.9,
                      "url" : "https://api.thousandeyes.com/v7/status",
                      "sendTime" : 8.1,
                      "receiveTime" : 224.1,
                      "connectTime" : 12.1,
                      "dnsTime" : 11.1,
                      "name" : "First Step to Acquire Token",
                      "stepNumber" : 1,
                      "assertions" : [ {
                        "hasFailed" : false,
                        "step" : 1
                      }, {
                        "hasFailed" : false,
                        "step" : 1
                      } ],
                      "assertErrorCount" : 0,
                      "blockedTime" : 49.9,
                      "stepTime" : 990.1,
                      "waitTime" : 18.1
                    }, {
                      "completion" : 100.0,
                      "stepType" : "default",
                      "responseTime" : 440.8,
                      "apiCallTime" : 900.9,
                      "processingTime" : 59.9,
                      "url" : "https://api.thousandeyes.com/v7/status",
                      "sendTime" : 8.1,
                      "receiveTime" : 224.1,
                      "connectTime" : 12.1,
                      "dnsTime" : 11.1,
                      "name" : "First Step to Acquire Token",
                      "stepNumber" : 1,
                      "assertions" : [ {
                        "hasFailed" : false,
                        "step" : 1
                      }, {
                        "hasFailed" : false,
                        "step" : 1
                      } ],
                      "assertErrorCount" : 0,
                      "blockedTime" : 49.9,
                      "stepTime" : 990.1,
                      "waitTime" : 18.1
                    } ],
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "completion" : 100.0,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "errorType" : "None",
                    "apiTransactionTime" : 990.1,
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "requests" : [ {
                      "completion" : 100.0,
                      "stepType" : "default",
                      "responseTime" : 440.8,
                      "apiCallTime" : 900.9,
                      "processingTime" : 59.9,
                      "url" : "https://api.thousandeyes.com/v7/status",
                      "sendTime" : 8.1,
                      "receiveTime" : 224.1,
                      "connectTime" : 12.1,
                      "dnsTime" : 11.1,
                      "name" : "First Step to Acquire Token",
                      "stepNumber" : 1,
                      "assertions" : [ {
                        "hasFailed" : false,
                        "step" : 1
                      }, {
                        "hasFailed" : false,
                        "step" : 1
                      } ],
                      "assertErrorCount" : 0,
                      "blockedTime" : 49.9,
                      "stepTime" : 990.1,
                      "waitTime" : 18.1
                    }, {
                      "completion" : 100.0,
                      "stepType" : "default",
                      "responseTime" : 440.8,
                      "apiCallTime" : 900.9,
                      "processingTime" : 59.9,
                      "url" : "https://api.thousandeyes.com/v7/status",
                      "sendTime" : 8.1,
                      "receiveTime" : 224.1,
                      "connectTime" : 12.1,
                      "dnsTime" : 11.1,
                      "name" : "First Step to Acquire Token",
                      "stepNumber" : 1,
                      "assertions" : [ {
                        "hasFailed" : false,
                        "step" : 1
                      }, {
                        "hasFailed" : false,
                        "step" : 1
                      } ],
                      "assertErrorCount" : 0,
                      "blockedTime" : 49.9,
                      "stepTime" : 990.1,
                      "waitTime" : 18.1
                    } ],
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.ApiDetailTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_test_api_results_models_validation(self) -> None:
        """Test case for get_test_api_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 60,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "endDate" : "2022-07-18T22:00:54Z",
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "completion" : 100.0,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "errorType" : "None",
                    "apiTransactionTime" : 990.1,
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "completion" : 100.0,
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "errorType" : "None",
                    "apiTransactionTime" : 990.1,
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.ApiTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
