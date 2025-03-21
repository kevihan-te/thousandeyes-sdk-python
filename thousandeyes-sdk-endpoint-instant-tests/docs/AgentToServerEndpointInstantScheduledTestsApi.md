# thousandeyes_sdk.endpoint_instant_tests.AgentToServerEndpointInstantScheduledTestsApi

All URIs are relative to *https://api.thousandeyes.com/v7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_to_server_scheduled_instant_test**](AgentToServerEndpointInstantScheduledTestsApi.md#create_agent_to_server_scheduled_instant_test) | **POST** /endpoint/tests/scheduled-tests/agent-to-server/instant | Run agent to server instant scheduled test


# **create_agent_to_server_scheduled_instant_test**
> EndpointAgentToServerTest create_agent_to_server_scheduled_instant_test(endpoint_agent_to_server_instant_test, aid=aid)

Run agent to server instant scheduled test

Creates and runs a new endpoint agent to server instant scheduled test in ThousandEyes.

### Example

* Bearer Authentication (BearerAuth):

```python
import thousandeyes_sdk.endpoint_instant_tests
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest
from thousandeyes_sdk.endpoint_instant_tests.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from thousandeyes_sdk.endpoint_instant_tests.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.thousandeyes.com/v7
# See configuration.py for a list of all supported configuration parameters.
configuration = thousandeyes_sdk.core.Configuration(
    host = "https://api.thousandeyes.com/v7"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = thousandeyes_sdk.core.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with thousandeyes_sdk.core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thousandeyes_sdk.endpoint_instant_tests.AgentToServerEndpointInstantScheduledTestsApi(api_client)
    endpoint_agent_to_server_instant_test = thousandeyes_sdk.endpoint_instant_tests.EndpointAgentToServerInstantTest() # EndpointAgentToServerInstantTest | 
    aid = '1234' # str | A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. (optional)

    try:
        # Run agent to server instant scheduled test
        api_response = api_instance.create_agent_to_server_scheduled_instant_test(endpoint_agent_to_server_instant_test, aid=aid)
        print("The response of AgentToServerEndpointInstantScheduledTestsApi->create_agent_to_server_scheduled_instant_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentToServerEndpointInstantScheduledTestsApi->create_agent_to_server_scheduled_instant_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_agent_to_server_instant_test** | [**EndpointAgentToServerInstantTest**](EndpointAgentToServerInstantTest.md)|  | 
 **aid** | **str**| A unique identifier associated with your account group. You can retrieve your &#x60;AccountGroupId&#x60; from the &#x60;/account-groups&#x60; endpoint. Note that you must be assigned to the target account group. Specifying this parameter without being assigned to the target account group will result in an error response. | [optional] 

### Return type

[**EndpointAgentToServerTest**](EndpointAgentToServerTest.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json, application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient permissions to query endpoint |  -  |
**429** | Exhausted rate limit for the organization |  -  |
**500** | Internal server error |  -  |
**502** | Bad Gateway |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

