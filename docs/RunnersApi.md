# peertube_api_client.RunnersApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_runners_get**](RunnersApi.md#api_v1_runners_get) | **GET** /api/v1/runners | List runners
[**api_v1_runners_register_post**](RunnersApi.md#api_v1_runners_register_post) | **POST** /api/v1/runners/register | Register a new runner
[**api_v1_runners_runner_id_delete**](RunnersApi.md#api_v1_runners_runner_id_delete) | **DELETE** /api/v1/runners/{runnerId} | Delete a runner
[**api_v1_runners_unregister_post**](RunnersApi.md#api_v1_runners_unregister_post) | **POST** /api/v1/runners/unregister | Unregister a runner


# **api_v1_runners_get**
> ApiV1RunnersGet200Response api_v1_runners_get(start=start, count=count, sort=sort)

List runners

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_get200_response import ApiV1RunnersGet200Response
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
    api_instance = peertube_api_client.RunnersApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort runners by criteria (optional)

    try:
        # List runners
        api_response = api_instance.api_v1_runners_get(start=start, count=count, sort=sort)
        print("The response of RunnersApi->api_v1_runners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->api_v1_runners_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort runners by criteria | [optional] 

### Return type

[**ApiV1RunnersGet200Response**](ApiV1RunnersGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_runners_register_post**
> ApiV1RunnersRegisterPost200Response api_v1_runners_register_post(api_v1_runners_register_post_request=api_v1_runners_register_post_request)

Register a new runner

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_register_post200_response import ApiV1RunnersRegisterPost200Response
from peertube_api_client.models.api_v1_runners_register_post_request import ApiV1RunnersRegisterPostRequest
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
    api_instance = peertube_api_client.RunnersApi(api_client)
    api_v1_runners_register_post_request = peertube_api_client.ApiV1RunnersRegisterPostRequest() # ApiV1RunnersRegisterPostRequest |  (optional)

    try:
        # Register a new runner
        api_response = api_instance.api_v1_runners_register_post(api_v1_runners_register_post_request=api_v1_runners_register_post_request)
        print("The response of RunnersApi->api_v1_runners_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunnersApi->api_v1_runners_register_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_runners_register_post_request** | [**ApiV1RunnersRegisterPostRequest**](ApiV1RunnersRegisterPostRequest.md)|  | [optional] 

### Return type

[**ApiV1RunnersRegisterPost200Response**](ApiV1RunnersRegisterPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_runners_runner_id_delete**
> api_v1_runners_runner_id_delete(runner_id, api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)

Delete a runner

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_unregister_post_request import ApiV1RunnersUnregisterPostRequest
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
    api_instance = peertube_api_client.RunnersApi(api_client)
    runner_id = 56 # int | 
    api_v1_runners_unregister_post_request = peertube_api_client.ApiV1RunnersUnregisterPostRequest() # ApiV1RunnersUnregisterPostRequest |  (optional)

    try:
        # Delete a runner
        api_instance.api_v1_runners_runner_id_delete(runner_id, api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)
    except Exception as e:
        print("Exception when calling RunnersApi->api_v1_runners_runner_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runner_id** | **int**|  | 
 **api_v1_runners_unregister_post_request** | [**ApiV1RunnersUnregisterPostRequest**](ApiV1RunnersUnregisterPostRequest.md)|  | [optional] 

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

# **api_v1_runners_unregister_post**
> api_v1_runners_unregister_post(api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)

Unregister a runner

API used by PeerTube runners

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_runners_unregister_post_request import ApiV1RunnersUnregisterPostRequest
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
    api_instance = peertube_api_client.RunnersApi(api_client)
    api_v1_runners_unregister_post_request = peertube_api_client.ApiV1RunnersUnregisterPostRequest() # ApiV1RunnersUnregisterPostRequest |  (optional)

    try:
        # Unregister a runner
        api_instance.api_v1_runners_unregister_post(api_v1_runners_unregister_post_request=api_v1_runners_unregister_post_request)
    except Exception as e:
        print("Exception when calling RunnersApi->api_v1_runners_unregister_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_runners_unregister_post_request** | [**ApiV1RunnersUnregisterPostRequest**](ApiV1RunnersUnregisterPostRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

