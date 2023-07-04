# peertube_api_client.VideoOwnershipChangeApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_videos_id_give_ownership_post**](VideoOwnershipChangeApi.md#api_v1_videos_id_give_ownership_post) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change
[**api_v1_videos_ownership_get**](VideoOwnershipChangeApi.md#api_v1_videos_ownership_get) | **GET** /api/v1/videos/ownership | List video ownership changes
[**api_v1_videos_ownership_id_accept_post**](VideoOwnershipChangeApi.md#api_v1_videos_ownership_id_accept_post) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request
[**api_v1_videos_ownership_id_refuse_post**](VideoOwnershipChangeApi.md#api_v1_videos_ownership_id_refuse_post) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request


# **api_v1_videos_id_give_ownership_post**
> api_v1_videos_id_give_ownership_post(id, username)

Request ownership change

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
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
    api_instance = peertube_api_client.VideoOwnershipChangeApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    username = 'username_example' # str | 

    try:
        # Request ownership change
        api_instance.api_v1_videos_id_give_ownership_post(id, username)
    except Exception as e:
        print("Exception when calling VideoOwnershipChangeApi->api_v1_videos_id_give_ownership_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | changing video ownership to a remote account is not supported yet |  -  |
**404** | video not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_ownership_get**
> api_v1_videos_ownership_get()

List video ownership changes

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
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
    api_instance = peertube_api_client.VideoOwnershipChangeApi(api_client)

    try:
        # List video ownership changes
        api_instance.api_v1_videos_ownership_get()
    except Exception as e:
        print("Exception when calling VideoOwnershipChangeApi->api_v1_videos_ownership_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_ownership_id_accept_post**
> api_v1_videos_ownership_id_accept_post(id)

Accept ownership change request

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
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
    api_instance = peertube_api_client.VideoOwnershipChangeApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Accept ownership change request
        api_instance.api_v1_videos_ownership_id_accept_post(id)
    except Exception as e:
        print("Exception when calling VideoOwnershipChangeApi->api_v1_videos_ownership_id_accept_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**403** | cannot terminate an ownership change of another user |  -  |
**404** | video ownership change not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_videos_ownership_id_refuse_post**
> api_v1_videos_ownership_id_refuse_post(id)

Refuse ownership change request

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
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
    api_instance = peertube_api_client.VideoOwnershipChangeApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Refuse ownership change request
        api_instance.api_v1_videos_ownership_id_refuse_post(id)
    except Exception as e:
        print("Exception when calling VideoOwnershipChangeApi->api_v1_videos_ownership_id_refuse_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**403** | cannot terminate an ownership change of another user |  -  |
**404** | video ownership change not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

