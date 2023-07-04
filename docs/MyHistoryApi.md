# peertube_api_client.MyHistoryApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_me_history_videos_get**](MyHistoryApi.md#api_v1_users_me_history_videos_get) | **GET** /api/v1/users/me/history/videos | List watched videos history
[**api_v1_users_me_history_videos_remove_post**](MyHistoryApi.md#api_v1_users_me_history_videos_remove_post) | **POST** /api/v1/users/me/history/videos/remove | Clear video history
[**api_v1_users_me_history_videos_video_id_delete**](MyHistoryApi.md#api_v1_users_me_history_videos_video_id_delete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element


# **api_v1_users_me_history_videos_get**
> VideoListResponse api_v1_users_me_history_videos_get(start=start, count=count, search=search)

List watched videos history

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
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
    api_instance = peertube_api_client.MyHistoryApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)

    try:
        # List watched videos history
        api_response = api_instance.api_v1_users_me_history_videos_get(start=start, count=count, search=search)
        print("The response of MyHistoryApi->api_v1_users_me_history_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyHistoryApi->api_v1_users_me_history_videos_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **api_v1_users_me_history_videos_remove_post**
> api_v1_users_me_history_videos_remove_post(before_date=before_date)

Clear video history

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
    api_instance = peertube_api_client.MyHistoryApi(api_client)
    before_date = '2013-10-20T19:20:30+01:00' # datetime | history before this date will be deleted (optional)

    try:
        # Clear video history
        api_instance.api_v1_users_me_history_videos_remove_post(before_date=before_date)
    except Exception as e:
        print("Exception when calling MyHistoryApi->api_v1_users_me_history_videos_remove_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before_date** | **datetime**| history before this date will be deleted | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_me_history_videos_video_id_delete**
> api_v1_users_me_history_videos_video_id_delete(video_id)

Delete history element

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
    api_instance = peertube_api_client.MyHistoryApi(api_client)
    video_id = 56 # int | 

    try:
        # Delete history element
        api_instance.api_v1_users_me_history_videos_video_id_delete(video_id)
    except Exception as e:
        print("Exception when calling MyHistoryApi->api_v1_users_me_history_videos_video_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

