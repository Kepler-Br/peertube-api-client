# peertube_api_client.StaticVideoFilesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**static_streaming_playlists_hls_filename_get**](StaticVideoFilesApi.md#static_streaming_playlists_hls_filename_get) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file
[**static_streaming_playlists_hls_private_filename_get**](StaticVideoFilesApi.md#static_streaming_playlists_hls_private_filename_get) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file
[**static_webseed_filename_get**](StaticVideoFilesApi.md#static_webseed_filename_get) | **GET** /static/webseed/{filename} | Get public WebTorrent video file
[**static_webseed_private_filename_get**](StaticVideoFilesApi.md#static_webseed_private_filename_get) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file


# **static_streaming_playlists_hls_filename_get**
> static_streaming_playlists_hls_filename_get(filename)

Get public HLS video file

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
    api_instance = peertube_api_client.StaticVideoFilesApi(api_client)
    filename = 'filename_example' # str | Filename

    try:
        # Get public HLS video file
        api_instance.static_streaming_playlists_hls_filename_get(filename)
    except Exception as e:
        print("Exception when calling StaticVideoFilesApi->static_streaming_playlists_hls_filename_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename | 

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
**403** | invalid auth |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_streaming_playlists_hls_private_filename_get**
> static_streaming_playlists_hls_private_filename_get(filename, video_file_token=video_file_token, reinject_video_file_token=reinject_video_file_token)

Get private HLS video file

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
    api_instance = peertube_api_client.StaticVideoFilesApi(api_client)
    filename = 'filename_example' # str | Filename
    video_file_token = 'video_file_token_example' # str | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header. (optional)
    reinject_video_file_token = True # bool | Ask the server to reinject videoFileToken in URLs in m3u8 playlist (optional)

    try:
        # Get private HLS video file
        api_instance.static_streaming_playlists_hls_private_filename_get(filename, video_file_token=video_file_token, reinject_video_file_token=reinject_video_file_token)
    except Exception as e:
        print("Exception when calling StaticVideoFilesApi->static_streaming_playlists_hls_private_filename_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename | 
 **video_file_token** | **str**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] 
 **reinject_video_file_token** | **bool**| Ask the server to reinject videoFileToken in URLs in m3u8 playlist | [optional] 

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
**403** | invalid auth |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_webseed_filename_get**
> static_webseed_filename_get(filename)

Get public WebTorrent video file

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.StaticVideoFilesApi(api_client)
    filename = 'filename_example' # str | Filename

    try:
        # Get public WebTorrent video file
        api_instance.static_webseed_filename_get(filename)
    except Exception as e:
        print("Exception when calling StaticVideoFilesApi->static_webseed_filename_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **static_webseed_private_filename_get**
> static_webseed_private_filename_get(filename, video_file_token=video_file_token)

Get private WebTorrent video file

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
    api_instance = peertube_api_client.StaticVideoFilesApi(api_client)
    filename = 'filename_example' # str | Filename
    video_file_token = 'video_file_token_example' # str | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header. (optional)

    try:
        # Get private WebTorrent video file
        api_instance.static_webseed_private_filename_get(filename, video_file_token=video_file_token)
    except Exception as e:
        print("Exception when calling StaticVideoFilesApi->static_webseed_private_filename_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename | 
 **video_file_token** | **str**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] 

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
**403** | invalid auth |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

