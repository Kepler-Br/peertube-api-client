# peertube_api_client.VideoMirroringApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**del_mirrored_video**](VideoMirroringApi.md#del_mirrored_video) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video
[**get_mirrored_videos**](VideoMirroringApi.md#get_mirrored_videos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored
[**put_mirrored_video**](VideoMirroringApi.md#put_mirrored_video) | **POST** /api/v1/server/redundancy/videos | Mirror a video


# **del_mirrored_video**
> del_mirrored_video(redundancy_id)

Delete a mirror done on a video

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
    api_instance = peertube_api_client.VideoMirroringApi(api_client)
    redundancy_id = 'redundancy_id_example' # str | id of an existing redundancy on a video

    try:
        # Delete a mirror done on a video
        api_instance.del_mirrored_video(redundancy_id)
    except Exception as e:
        print("Exception when calling VideoMirroringApi->del_mirrored_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redundancy_id** | **str**| id of an existing redundancy on a video | 

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
**404** | video redundancy not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mirrored_videos**
> List[VideoRedundancy] get_mirrored_videos(target, start=start, count=count, sort=sort)

List videos being mirrored

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_redundancy import VideoRedundancy
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
    api_instance = peertube_api_client.VideoMirroringApi(api_client)
    target = 'target_example' # str | direction of the mirror
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort abuses by criteria (optional)

    try:
        # List videos being mirrored
        api_response = api_instance.get_mirrored_videos(target, start=start, count=count, sort=sort)
        print("The response of VideoMirroringApi->get_mirrored_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoMirroringApi->get_mirrored_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| direction of the mirror | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort abuses by criteria | [optional] 

### Return type

[**List[VideoRedundancy]**](VideoRedundancy.md)

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

# **put_mirrored_video**
> put_mirrored_video(put_mirrored_video_request=put_mirrored_video_request)

Mirror a video

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.put_mirrored_video_request import PutMirroredVideoRequest
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
    api_instance = peertube_api_client.VideoMirroringApi(api_client)
    put_mirrored_video_request = peertube_api_client.PutMirroredVideoRequest() # PutMirroredVideoRequest |  (optional)

    try:
        # Mirror a video
        api_instance.put_mirrored_video(put_mirrored_video_request=put_mirrored_video_request)
    except Exception as e:
        print("Exception when calling VideoMirroringApi->put_mirrored_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_mirrored_video_request** | [**PutMirroredVideoRequest**](PutMirroredVideoRequest.md)|  | [optional] 

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
**400** | cannot mirror a local video |  -  |
**404** | video does not exist |  -  |
**409** | video is already mirrored |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

