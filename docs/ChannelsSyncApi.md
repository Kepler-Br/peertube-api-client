# peertube_api_client.ChannelsSyncApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_video_channel_sync**](ChannelsSyncApi.md#add_video_channel_sync) | **POST** /api/v1/video-channel-syncs | Create a synchronization for a video channel
[**api_v1_accounts_name_video_channel_syncs_get**](ChannelsSyncApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**api_v1_video_channels_channel_handle_import_videos_post**](ChannelsSyncApi.md#api_v1_video_channels_channel_handle_import_videos_post) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
[**del_video_channel_sync**](ChannelsSyncApi.md#del_video_channel_sync) | **DELETE** /api/v1/video-channel-syncs/{channelSyncId} | Delete a video channel synchronization
[**trigger_video_channel_sync**](ChannelsSyncApi.md#trigger_video_channel_sync) | **POST** /api/v1/video-channel-syncs/{channelSyncId}/sync | Triggers the channel synchronization job, fetching all the videos from the remote channel


# **add_video_channel_sync**
> AddVideoChannelSync200Response add_video_channel_sync(video_channel_sync_create=video_channel_sync_create)

Create a synchronization for a video channel

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_video_channel_sync200_response import AddVideoChannelSync200Response
from peertube_api_client.models.video_channel_sync_create import VideoChannelSyncCreate
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
    api_instance = peertube_api_client.ChannelsSyncApi(api_client)
    video_channel_sync_create = peertube_api_client.VideoChannelSyncCreate() # VideoChannelSyncCreate |  (optional)

    try:
        # Create a synchronization for a video channel
        api_response = api_instance.add_video_channel_sync(video_channel_sync_create=video_channel_sync_create)
        print("The response of ChannelsSyncApi->add_video_channel_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsSyncApi->add_video_channel_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_channel_sync_create** | [**VideoChannelSyncCreate**](VideoChannelSyncCreate.md)|  | [optional] 

### Return type

[**AddVideoChannelSync200Response**](AddVideoChannelSync200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_accounts_name_video_channel_syncs_get**
> VideoChannelSyncList api_v1_accounts_name_video_channel_syncs_get(name, start=start, count=count, sort=sort)

List the synchronizations of video channels of an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_sync_list import VideoChannelSyncList
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
    api_instance = peertube_api_client.ChannelsSyncApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List the synchronizations of video channels of an account
        api_response = api_instance.api_v1_accounts_name_video_channel_syncs_get(name, start=start, count=count, sort=sort)
        print("The response of ChannelsSyncApi->api_v1_accounts_name_video_channel_syncs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsSyncApi->api_v1_accounts_name_video_channel_syncs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelSyncList**](VideoChannelSyncList.md)

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

# **api_v1_video_channels_channel_handle_import_videos_post**
> api_v1_video_channels_channel_handle_import_videos_post(channel_handle, import_videos_in_channel_create=import_videos_in_channel_create)

Import videos in channel

Import a remote channel/playlist videos into a channel

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.import_videos_in_channel_create import ImportVideosInChannelCreate
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
    api_instance = peertube_api_client.ChannelsSyncApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    import_videos_in_channel_create = peertube_api_client.ImportVideosInChannelCreate() # ImportVideosInChannelCreate |  (optional)

    try:
        # Import videos in channel
        api_instance.api_v1_video_channels_channel_handle_import_videos_post(channel_handle, import_videos_in_channel_create=import_videos_in_channel_create)
    except Exception as e:
        print("Exception when calling ChannelsSyncApi->api_v1_video_channels_channel_handle_import_videos_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **import_videos_in_channel_create** | [**ImportVideosInChannelCreate**](ImportVideosInChannelCreate.md)|  | [optional] 

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

# **del_video_channel_sync**
> del_video_channel_sync(channel_sync_id)

Delete a video channel synchronization

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
    api_instance = peertube_api_client.ChannelsSyncApi(api_client)
    channel_sync_id = 56 # int | Channel Sync id

    try:
        # Delete a video channel synchronization
        api_instance.del_video_channel_sync(channel_sync_id)
    except Exception as e:
        print("Exception when calling ChannelsSyncApi->del_video_channel_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_sync_id** | **int**| Channel Sync id | 

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

# **trigger_video_channel_sync**
> trigger_video_channel_sync(channel_sync_id)

Triggers the channel synchronization job, fetching all the videos from the remote channel

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
    api_instance = peertube_api_client.ChannelsSyncApi(api_client)
    channel_sync_id = 56 # int | Channel Sync id

    try:
        # Triggers the channel synchronization job, fetching all the videos from the remote channel
        api_instance.trigger_video_channel_sync(channel_sync_id)
    except Exception as e:
        print("Exception when calling ChannelsSyncApi->trigger_video_channel_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_sync_id** | **int**| Channel Sync id | 

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

