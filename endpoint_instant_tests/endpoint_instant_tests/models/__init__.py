# coding: utf-8

# flake8: noqa
"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from endpoint_instant_tests.models.account_group_id import AccountGroupId
from endpoint_instant_tests.models.alert_direction import AlertDirection
from endpoint_instant_tests.models.alert_rounds_violation_mode import AlertRoundsViolationMode
from endpoint_instant_tests.models.alert_rule import AlertRule
from endpoint_instant_tests.models.alert_type import AlertType
from endpoint_instant_tests.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from endpoint_instant_tests.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from endpoint_instant_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest
from endpoint_instant_tests.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from endpoint_instant_tests.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from endpoint_instant_tests.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest
from endpoint_instant_tests.models.endpoint_http_server_instant_test import EndpointHttpServerInstantTest
from endpoint_instant_tests.models.endpoint_http_server_test import EndpointHttpServerTest
from endpoint_instant_tests.models.endpoint_instant_test import EndpointInstantTest
from endpoint_instant_tests.models.endpoint_scheduled_test_type import EndpointScheduledTestType
from endpoint_instant_tests.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from endpoint_instant_tests.models.endpoint_test import EndpointTest
from endpoint_instant_tests.models.endpoint_test_agent_selector_type import EndpointTestAgentSelectorType
from endpoint_instant_tests.models.endpoint_test_auth_type import EndpointTestAuthType
from endpoint_instant_tests.models.endpoint_test_links import EndpointTestLinks
from endpoint_instant_tests.models.endpoint_test_links_self import EndpointTestLinksSelf
from endpoint_instant_tests.models.endpoint_test_protocol import EndpointTestProtocol
from endpoint_instant_tests.models.error import Error
from endpoint_instant_tests.models.link import Link
from endpoint_instant_tests.models.severity import Severity
from endpoint_instant_tests.models.test_interval import TestInterval
from endpoint_instant_tests.models.test_labels_inner import TestLabelsInner
from endpoint_instant_tests.models.test_probe_mode_response import TestProbeModeResponse
from endpoint_instant_tests.models.test_ssl_version_id import TestSslVersionId
from endpoint_instant_tests.models.unauthorized_error import UnauthorizedError
from endpoint_instant_tests.models.validation_error import ValidationError
from endpoint_instant_tests.models.validation_error_all_of_errors import ValidationErrorAllOfErrors
