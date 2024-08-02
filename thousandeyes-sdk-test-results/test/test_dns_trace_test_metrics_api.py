# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.13
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.dns_trace_test_metrics_api import DNSTraceTestMetricsApi


class TestDNSTraceTestMetricsApi(unittest.TestCase):
    """DNSTraceTestMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DNSTraceTestMetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_dns_trace_results_models_validation(self) -> None:
        """Test case for get_test_dns_trace_results request and response models"""

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
                    "interval" : 120,
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
                    "finalServerQueried" : "a1.verisigndns.com.",
                    "finalQueryTime" : 178,
                    "queries" : 3,
                    "failedQueries" : 0,
                    "output" : "com.\\t172800\\tIN\\tNS\\ta.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tf.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tc.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tb.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\td.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\te.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tg.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tm.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\th.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tj.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\ti.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tl.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tk.gtld-servers.net.\\n;; Received 498 bytes from 199.7.91.13(d.root-servers.net.) in 119 ms\\n\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta1.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta2.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta3.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\tu1.verisigndns.com.\\n;; Received 266 bytes from 192.5.6.30(a.gtld-servers.net.) in 178 ms\\n\\napp.thousandeyes.com.\\t300\\tIN\\tCNAME\\tweb.thousandeyes.com.\\nweb.thousandeyes.com.\\t300\\tIN\\tCNAME\\tlb-app.thousandeyes.com.\\nlb-app.thousandeyes.com.\\t3600\\tIN\\tA\\t208.185.7.120\\n;; Received 173 bytes from 209.112.113.33(a1.verisigndns.com.) in 178 ms\\n\\n",
                    "mappings" : "208.185.7.120",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
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
                    "finalServerQueried" : "a1.verisigndns.com.",
                    "finalQueryTime" : 178,
                    "queries" : 3,
                    "failedQueries" : 0,
                    "output" : "com.\\t172800\\tIN\\tNS\\ta.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tf.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tc.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tb.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\td.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\te.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tg.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tm.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\th.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tj.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\ti.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tl.gtld-servers.net.\\ncom.\\t172800\\tIN\\tNS\\tk.gtld-servers.net.\\n;; Received 498 bytes from 199.7.91.13(d.root-servers.net.) in 119 ms\\n\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta1.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta2.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\ta3.verisigndns.com.\\nthousandeyes.com.\\t172800\\tIN\\tNS\\tu1.verisigndns.com.\\n;; Received 266 bytes from 192.5.6.30(a.gtld-servers.net.) in 178 ms\\n\\napp.thousandeyes.com.\\t300\\tIN\\tCNAME\\tweb.thousandeyes.com.\\nweb.thousandeyes.com.\\t300\\tIN\\tCNAME\\tlb-app.thousandeyes.com.\\nlb-app.thousandeyes.com.\\t3600\\tIN\\tA\\t208.185.7.120\\n;; Received 173 bytes from 209.112.113.33(a1.verisigndns.com.) in 178 ms\\n\\n",
                    "mappings" : "208.185.7.120",
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "errorDetails" : "Connection error"
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.DnsTraceTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
