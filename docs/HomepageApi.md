# peertube_api_client.HomepageApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_custom_pages_homepage_instance_get**](HomepageApi.md#api_v1_custom_pages_homepage_instance_get) | **GET** /api/v1/custom-pages/homepage/instance | Get instance custom homepage
[**api_v1_custom_pages_homepage_instance_put**](HomepageApi.md#api_v1_custom_pages_homepage_instance_put) | **PUT** /api/v1/custom-pages/homepage/instance | Set instance custom homepage


# **api_v1_custom_pages_homepage_instance_get**
> CustomHomepage api_v1_custom_pages_homepage_instance_get()

Get instance custom homepage

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.custom_homepage import CustomHomepage
from peertube_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://peertube2.cpy.re
# See configuration.py for a list of all supported configuration parameters.
configuration = peertube_api_client.Configuration(
    host = "https://peertube2.cpy.re"
)


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.HomepageApi(api_client)

    try:
        # Get instance custom homepage
        api_response = api_instance.api_v1_custom_pages_homepage_instance_get()
        print("The response of HomepageApi->api_v1_custom_pages_homepage_instance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HomepageApi->api_v1_custom_pages_homepage_instance_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomHomepage**](CustomHomepage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | No homepage set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_custom_pages_homepage_instance_put**
> api_v1_custom_pages_homepage_instance_put(api_v1_custom_pages_homepage_instance_put_request=api_v1_custom_pages_homepage_instance_put_request)

Set instance custom homepage

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_custom_pages_homepage_instance_put_request import ApiV1CustomPagesHomepageInstancePutRequest
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
    api_instance = peertube_api_client.HomepageApi(api_client)
    api_v1_custom_pages_homepage_instance_put_request = peertube_api_client.ApiV1CustomPagesHomepageInstancePutRequest() # ApiV1CustomPagesHomepageInstancePutRequest |  (optional)

    try:
        # Set instance custom homepage
        api_instance.api_v1_custom_pages_homepage_instance_put(api_v1_custom_pages_homepage_instance_put_request=api_v1_custom_pages_homepage_instance_put_request)
    except Exception as e:
        print("Exception when calling HomepageApi->api_v1_custom_pages_homepage_instance_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_custom_pages_homepage_instance_put_request** | [**ApiV1CustomPagesHomepageInstancePutRequest**](ApiV1CustomPagesHomepageInstancePutRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

