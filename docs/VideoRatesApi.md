# peertube_api_client.VideoRatesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_me_videos_video_id_rating_get**](VideoRatesApi.md#api_v1_users_me_videos_video_id_rating_get) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
[**api_v1_videos_id_rate_put**](VideoRatesApi.md#api_v1_videos_id_rate_put) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video


# **api_v1_users_me_videos_video_id_rating_get**
> GetMeVideoRating api_v1_users_me_videos_video_id_rating_get(video_id)

Get rate of my user for a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_me_video_rating import GetMeVideoRating
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
    api_instance = peertube_api_client.VideoRatesApi(api_client)
    video_id = 56 # int | The video id

    try:
        # Get rate of my user for a video
        api_response = api_instance.api_v1_users_me_videos_video_id_rating_get(video_id)
        print("The response of VideoRatesApi->api_v1_users_me_videos_video_id_rating_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoRatesApi->api_v1_users_me_videos_video_id_rating_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

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

# **api_v1_videos_id_rate_put**
> api_v1_videos_id_rate_put(id, api_v1_videos_id_rate_put_request=api_v1_videos_id_rate_put_request)

Like/dislike a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_videos_id_rate_put_request import ApiV1VideosIdRatePutRequest
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
    api_instance = peertube_api_client.VideoRatesApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    api_v1_videos_id_rate_put_request = peertube_api_client.ApiV1VideosIdRatePutRequest() # ApiV1VideosIdRatePutRequest |  (optional)

    try:
        # Like/dislike a video
        api_instance.api_v1_videos_id_rate_put(id, api_v1_videos_id_rate_put_request=api_v1_videos_id_rate_put_request)
    except Exception as e:
        print("Exception when calling VideoRatesApi->api_v1_videos_id_rate_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **api_v1_videos_id_rate_put_request** | [**ApiV1VideosIdRatePutRequest**](ApiV1VideosIdRatePutRequest.md)|  | [optional] 

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
**404** | video does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

