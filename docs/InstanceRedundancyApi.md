# peertube_api_client.InstanceRedundancyApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_server_redundancy_host_put**](InstanceRedundancyApi.md#api_v1_server_redundancy_host_put) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy


# **api_v1_server_redundancy_host_put**
> api_v1_server_redundancy_host_put(host, api_v1_server_redundancy_host_put_request=api_v1_server_redundancy_host_put_request)

Update a server redundancy policy

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_server_redundancy_host_put_request import ApiV1ServerRedundancyHostPutRequest
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.InstanceRedundancyApi(api_client)
    host = 'host_example' # str | server domain to mirror
    api_v1_server_redundancy_host_put_request = peertube_api_client.ApiV1ServerRedundancyHostPutRequest() # ApiV1ServerRedundancyHostPutRequest |  (optional)

    try:
        # Update a server redundancy policy
        api_instance.api_v1_server_redundancy_host_put(host, api_v1_server_redundancy_host_put_request=api_v1_server_redundancy_host_put_request)
    except Exception as e:
        print("Exception when calling InstanceRedundancyApi->api_v1_server_redundancy_host_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| server domain to mirror | 
 **api_v1_server_redundancy_host_put_request** | [**ApiV1ServerRedundancyHostPutRequest**](ApiV1ServerRedundancyHostPutRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**404** | server is not already known |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

