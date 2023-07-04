# peertube_api_client.VideoTranscodingApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_videos_id_studio_edit_post**](VideoTranscodingApi.md#api_v1_videos_id_studio_edit_post) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task
[**create_video_transcoding**](VideoTranscodingApi.md#create_video_transcoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job


# **api_v1_videos_id_studio_edit_post**
> api_v1_videos_id_studio_edit_post(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

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
    api_instance = peertube_api_client.VideoTranscodingApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Create a studio task
        api_instance.api_v1_videos_id_studio_edit_post(id)
    except Exception as e:
        print("Exception when calling VideoTranscodingApi->api_v1_videos_id_studio_edit_post: %s\n" % e)
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

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | incorrect parameters |  -  |
**404** | video not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video_transcoding**
> create_video_transcoding(id, create_video_transcoding_request=create_video_transcoding_request)

Create a transcoding job

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.create_video_transcoding_request import CreateVideoTranscodingRequest
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
    api_instance = peertube_api_client.VideoTranscodingApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid
    create_video_transcoding_request = peertube_api_client.CreateVideoTranscodingRequest() # CreateVideoTranscodingRequest |  (optional)

    try:
        # Create a transcoding job
        api_instance.create_video_transcoding(id, create_video_transcoding_request=create_video_transcoding_request)
    except Exception as e:
        print("Exception when calling VideoTranscodingApi->create_video_transcoding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**ApiV1VideosOwnershipIdAcceptPostIdParameter**](.md)| The object id, uuid or short uuid | 
 **create_video_transcoding_request** | [**CreateVideoTranscodingRequest**](CreateVideoTranscodingRequest.md)|  | [optional] 

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

