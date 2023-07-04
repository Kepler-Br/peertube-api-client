# peertube_api_client.VideoBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_video_block**](VideoBlocksApi.md#add_video_block) | **POST** /api/v1/videos/{id}/blacklist | Block a video
[**del_video_block**](VideoBlocksApi.md#del_video_block) | **DELETE** /api/v1/videos/{id}/blacklist | Unblock a video by its id
[**get_video_blocks**](VideoBlocksApi.md#get_video_blocks) | **GET** /api/v1/videos/blacklist | List video blocks


# **add_video_block**
> add_video_block(id)

Block a video

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
    api_instance = peertube_api_client.VideoBlocksApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Block a video
        api_instance.add_video_block(id)
    except Exception as e:
        print("Exception when calling VideoBlocksApi->add_video_block: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_video_block**
> del_video_block(id)

Unblock a video by its id

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
    api_instance = peertube_api_client.VideoBlocksApi(api_client)
    id = peertube_api_client.ApiV1VideosOwnershipIdAcceptPostIdParameter() # ApiV1VideosOwnershipIdAcceptPostIdParameter | The object id, uuid or short uuid

    try:
        # Unblock a video by its id
        api_instance.del_video_block(id)
    except Exception as e:
        print("Exception when calling VideoBlocksApi->del_video_block: %s\n" % e)
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
**404** | block not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_blocks**
> GetVideoBlocks200Response get_video_blocks(type=type, search=search, start=start, count=count, sort=sort)

List video blocks

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.get_video_blocks200_response import GetVideoBlocks200Response
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
    api_instance = peertube_api_client.VideoBlocksApi(api_client)
    type = 56 # int | list only blocks that match this type: - `1`: manual block - `2`: automatic block that needs review  (optional)
    search = 'search_example' # str | plain search that will match with video titles, and more (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort blocklists by criteria (optional)

    try:
        # List video blocks
        api_response = api_instance.get_video_blocks(type=type, search=search, start=start, count=count, sort=sort)
        print("The response of VideoBlocksApi->get_video_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoBlocksApi->get_video_blocks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **int**| list only blocks that match this type: - &#x60;1&#x60;: manual block - &#x60;2&#x60;: automatic block that needs review  | [optional] 
 **search** | **str**| plain search that will match with video titles, and more | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort blocklists by criteria | [optional] 

### Return type

[**GetVideoBlocks200Response**](GetVideoBlocks200Response.md)

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

