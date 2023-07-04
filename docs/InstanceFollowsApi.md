# peertube_api_client.InstanceFollowsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_server_followers_get**](InstanceFollowsApi.md#api_v1_server_followers_get) | **GET** /api/v1/server/followers | List instances following the server
[**api_v1_server_followers_name_with_host_accept_post**](InstanceFollowsApi.md#api_v1_server_followers_name_with_host_accept_post) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server
[**api_v1_server_followers_name_with_host_delete**](InstanceFollowsApi.md#api_v1_server_followers_name_with_host_delete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server
[**api_v1_server_followers_name_with_host_reject_post**](InstanceFollowsApi.md#api_v1_server_followers_name_with_host_reject_post) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server
[**api_v1_server_following_get**](InstanceFollowsApi.md#api_v1_server_following_get) | **GET** /api/v1/server/following | List instances followed by the server
[**api_v1_server_following_host_or_handle_delete**](InstanceFollowsApi.md#api_v1_server_following_host_or_handle_delete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account)
[**api_v1_server_following_post**](InstanceFollowsApi.md#api_v1_server_following_post) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account)


# **api_v1_server_followers_get**
> GetAccountFollowers200Response api_v1_server_followers_get(state=state, actor_type=actor_type, start=start, count=count, sort=sort)

List instances following the server

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_account_followers200_response import GetAccountFollowers200Response
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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    state = 'state_example' # str |  (optional)
    actor_type = 'actor_type_example' # str |  (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List instances following the server
        api_response = api_instance.api_v1_server_followers_get(state=state, actor_type=actor_type, start=start, count=count, sort=sort)
        print("The response of InstanceFollowsApi->api_v1_server_followers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_followers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional] 
 **actor_type** | **str**|  | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_followers_name_with_host_accept_post**
> api_v1_server_followers_name_with_host_accept_post(name_with_host)

Accept a pending follower to your server

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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    name_with_host = 'name_with_host_example' # str | The remote actor handle to remove from your followers

    try:
        # Accept a pending follower to your server
        api_instance.api_v1_server_followers_name_with_host_accept_post(name_with_host)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_followers_name_with_host_accept_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_with_host** | **str**| The remote actor handle to remove from your followers | 

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
**404** | follower not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_followers_name_with_host_delete**
> api_v1_server_followers_name_with_host_delete(name_with_host)

Remove or reject a follower to your server

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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    name_with_host = 'name_with_host_example' # str | The remote actor handle to remove from your followers

    try:
        # Remove or reject a follower to your server
        api_instance.api_v1_server_followers_name_with_host_delete(name_with_host)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_followers_name_with_host_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_with_host** | **str**| The remote actor handle to remove from your followers | 

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
**404** | follower not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_followers_name_with_host_reject_post**
> api_v1_server_followers_name_with_host_reject_post(name_with_host)

Reject a pending follower to your server

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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    name_with_host = 'name_with_host_example' # str | The remote actor handle to remove from your followers

    try:
        # Reject a pending follower to your server
        api_instance.api_v1_server_followers_name_with_host_reject_post(name_with_host)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_followers_name_with_host_reject_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_with_host** | **str**| The remote actor handle to remove from your followers | 

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
**404** | follower not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_following_get**
> GetAccountFollowers200Response api_v1_server_following_get(state=state, actor_type=actor_type, start=start, count=count, sort=sort)

List instances followed by the server

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_account_followers200_response import GetAccountFollowers200Response
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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    state = 'state_example' # str |  (optional)
    actor_type = 'actor_type_example' # str |  (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List instances followed by the server
        api_response = api_instance.api_v1_server_following_get(state=state, actor_type=actor_type, start=start, count=count, sort=sort)
        print("The response of InstanceFollowsApi->api_v1_server_following_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_following_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional] 
 **actor_type** | **str**|  | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_following_host_or_handle_delete**
> api_v1_server_following_host_or_handle_delete(host_or_handle)

Unfollow an actor (PeerTube instance, channel or account)

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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    host_or_handle = 'host_or_handle_example' # str | The hostOrHandle to unfollow

    try:
        # Unfollow an actor (PeerTube instance, channel or account)
        api_instance.api_v1_server_following_host_or_handle_delete(host_or_handle)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_following_host_or_handle_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_or_handle** | **str**| The hostOrHandle to unfollow | 

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
**404** | host or handle not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_server_following_post**
> api_v1_server_following_post(api_v1_server_following_post_request=api_v1_server_following_post_request)

Follow a list of actors (PeerTube instance, channel or account)

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_server_following_post_request import ApiV1ServerFollowingPostRequest
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
    api_instance = peertube_api_client.InstanceFollowsApi(api_client)
    api_v1_server_following_post_request = peertube_api_client.ApiV1ServerFollowingPostRequest() # ApiV1ServerFollowingPostRequest |  (optional)

    try:
        # Follow a list of actors (PeerTube instance, channel or account)
        api_instance.api_v1_server_following_post(api_v1_server_following_post_request=api_v1_server_following_post_request)
    except Exception as e:
        print("Exception when calling InstanceFollowsApi->api_v1_server_following_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v1_server_following_post_request** | [**ApiV1ServerFollowingPostRequest**](ApiV1ServerFollowingPostRequest.md)|  | [optional] 

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
**500** | cannot follow a non-HTTPS server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

