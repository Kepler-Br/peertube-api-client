# peertube_api_client.VideoChannelsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_video_channel**](VideoChannelsApi.md#add_video_channel) | **POST** /api/v1/video-channels | Create a video channel
[**api_v1_accounts_name_video_channel_syncs_get**](VideoChannelsApi.md#api_v1_accounts_name_video_channel_syncs_get) | **GET** /api/v1/accounts/{name}/video-channel-syncs | List the synchronizations of video channels of an account
[**api_v1_accounts_name_video_channels_get**](VideoChannelsApi.md#api_v1_accounts_name_video_channels_get) | **GET** /api/v1/accounts/{name}/video-channels | List video channels of an account
[**api_v1_video_channels_channel_handle_avatar_delete**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_avatar_delete) | **DELETE** /api/v1/video-channels/{channelHandle}/avatar | Delete channel avatar
[**api_v1_video_channels_channel_handle_avatar_pick_post**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_avatar_pick_post) | **POST** /api/v1/video-channels/{channelHandle}/avatar/pick | Update channel avatar
[**api_v1_video_channels_channel_handle_banner_delete**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_banner_delete) | **DELETE** /api/v1/video-channels/{channelHandle}/banner | Delete channel banner
[**api_v1_video_channels_channel_handle_banner_pick_post**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_banner_pick_post) | **POST** /api/v1/video-channels/{channelHandle}/banner/pick | Update channel banner
[**api_v1_video_channels_channel_handle_import_videos_post**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_import_videos_post) | **POST** /api/v1/video-channels/{channelHandle}/import-videos | Import videos in channel
[**api_v1_video_channels_channel_handle_video_playlists_get**](VideoChannelsApi.md#api_v1_video_channels_channel_handle_video_playlists_get) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
[**del_video_channel**](VideoChannelsApi.md#del_video_channel) | **DELETE** /api/v1/video-channels/{channelHandle} | Delete a video channel
[**get_video_channel**](VideoChannelsApi.md#get_video_channel) | **GET** /api/v1/video-channels/{channelHandle} | Get a video channel
[**get_video_channel_followers**](VideoChannelsApi.md#get_video_channel_followers) | **GET** /api/v1/video-channels/{channelHandle}/followers | List followers of a video channel
[**get_video_channel_videos**](VideoChannelsApi.md#get_video_channel_videos) | **GET** /api/v1/video-channels/{channelHandle}/videos | List videos of a video channel
[**get_video_channels**](VideoChannelsApi.md#get_video_channels) | **GET** /api/v1/video-channels | List video channels
[**put_video_channel**](VideoChannelsApi.md#put_video_channel) | **PUT** /api/v1/video-channels/{channelHandle} | Update a video channel


# **add_video_channel**
> AddVideoChannel200Response add_video_channel(video_channel_create=video_channel_create)

Create a video channel

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_video_channel200_response import AddVideoChannel200Response
from peertube_api_client.models.video_channel_create import VideoChannelCreate
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    video_channel_create = peertube_api_client.VideoChannelCreate() # VideoChannelCreate |  (optional)

    try:
        # Create a video channel
        api_response = api_instance.add_video_channel(video_channel_create=video_channel_create)
        print("The response of VideoChannelsApi->add_video_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->add_video_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_channel_create** | [**VideoChannelCreate**](VideoChannelCreate.md)|  | [optional] 

### Return type

[**AddVideoChannel200Response**](AddVideoChannel200Response.md)

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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List the synchronizations of video channels of an account
        api_response = api_instance.api_v1_accounts_name_video_channel_syncs_get(name, start=start, count=count, sort=sort)
        print("The response of VideoChannelsApi->api_v1_accounts_name_video_channel_syncs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_accounts_name_video_channel_syncs_get: %s\n" % e)
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

# **api_v1_accounts_name_video_channels_get**
> VideoChannelList api_v1_accounts_name_video_channels_get(name, with_stats=with_stats, start=start, count=count, sort=sort)

List video channels of an account

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_list import VideoChannelList
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    with_stats = True # bool | include daily view statistics for the last 30 days and total views (only if authentified as the account user) (optional)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List video channels of an account
        api_response = api_instance.api_v1_accounts_name_video_channels_get(name, with_stats=with_stats, start=start, count=count, sort=sort)
        print("The response of VideoChannelsApi->api_v1_accounts_name_video_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_accounts_name_video_channels_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **with_stats** | **bool**| include daily view statistics for the last 30 days and total views (only if authentified as the account user) | [optional] 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelList**](VideoChannelList.md)

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

# **api_v1_video_channels_channel_handle_avatar_delete**
> api_v1_video_channels_channel_handle_avatar_delete(channel_handle)

Delete channel avatar

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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle

    try:
        # Delete channel avatar
        api_instance.api_v1_video_channels_channel_handle_avatar_delete(channel_handle)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_avatar_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 

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

# **api_v1_video_channels_channel_handle_avatar_pick_post**
> ApiV1UsersMeAvatarPickPost200Response api_v1_video_channels_channel_handle_avatar_pick_post(channel_handle, avatarfile=avatarfile)

Update channel avatar

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_avatar_pick_post200_response import ApiV1UsersMeAvatarPickPost200Response
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    avatarfile = None # bytearray | The file to upload. (optional)

    try:
        # Update channel avatar
        api_response = api_instance.api_v1_video_channels_channel_handle_avatar_pick_post(channel_handle, avatarfile=avatarfile)
        print("The response of VideoChannelsApi->api_v1_video_channels_channel_handle_avatar_pick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_avatar_pick_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **avatarfile** | **bytearray**| The file to upload. | [optional] 

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the banner <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_video_channels_channel_handle_banner_delete**
> api_v1_video_channels_channel_handle_banner_delete(channel_handle)

Delete channel banner

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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle

    try:
        # Delete channel banner
        api_instance.api_v1_video_channels_channel_handle_banner_delete(channel_handle)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_banner_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 

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

# **api_v1_video_channels_channel_handle_banner_pick_post**
> ApiV1VideoChannelsChannelHandleBannerPickPost200Response api_v1_video_channels_channel_handle_banner_pick_post(channel_handle, bannerfile=bannerfile)

Update channel banner

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_video_channels_channel_handle_banner_pick_post200_response import ApiV1VideoChannelsChannelHandleBannerPickPost200Response
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    bannerfile = None # bytearray | The file to upload. (optional)

    try:
        # Update channel banner
        api_response = api_instance.api_v1_video_channels_channel_handle_banner_pick_post(channel_handle, bannerfile=bannerfile)
        print("The response of VideoChannelsApi->api_v1_video_channels_channel_handle_banner_pick_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_banner_pick_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **bannerfile** | **bytearray**| The file to upload. | [optional] 

### Return type

[**ApiV1VideoChannelsChannelHandleBannerPickPost200Response**](ApiV1VideoChannelsChannelHandleBannerPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**413** | image file too large |  * X-File-Maximum-Size - Maximum file size for the banner <br>  |

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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    import_videos_in_channel_create = peertube_api_client.ImportVideosInChannelCreate() # ImportVideosInChannelCreate |  (optional)

    try:
        # Import videos in channel
        api_instance.api_v1_video_channels_channel_handle_import_videos_post(channel_handle, import_videos_in_channel_create=import_videos_in_channel_create)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_import_videos_post: %s\n" % e)
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

# **api_v1_video_channels_channel_handle_video_playlists_get**
> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response api_v1_video_channels_channel_handle_video_playlists_get(channel_handle, start=start, count=count, sort=sort, playlist_type=playlist_type)

List playlists of a channel

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_video_channels_channel_handle_video_playlists_get200_response import ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
from peertube_api_client.models.video_playlist_type_set import VideoPlaylistTypeSet
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    playlist_type = peertube_api_client.VideoPlaylistTypeSet() # VideoPlaylistTypeSet |  (optional)

    try:
        # List playlists of a channel
        api_response = api_instance.api_v1_video_channels_channel_handle_video_playlists_get(channel_handle, start=start, count=count, sort=sort, playlist_type=playlist_type)
        print("The response of VideoChannelsApi->api_v1_video_channels_channel_handle_video_playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->api_v1_video_channels_channel_handle_video_playlists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **playlist_type** | [**VideoPlaylistTypeSet**](.md)|  | [optional] 

### Return type

[**ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response**](ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response.md)

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

# **del_video_channel**
> del_video_channel(channel_handle)

Delete a video channel

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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle

    try:
        # Delete a video channel
        api_instance.del_video_channel(channel_handle)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->del_video_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 

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

# **get_video_channel**
> VideoChannel get_video_channel(channel_handle)

Get a video channel

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel import VideoChannel
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle

    try:
        # Get a video channel
        api_response = api_instance.get_video_channel(channel_handle)
        print("The response of VideoChannelsApi->get_video_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->get_video_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 

### Return type

[**VideoChannel**](VideoChannel.md)

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

# **get_video_channel_followers**
> GetAccountFollowers200Response get_video_channel_followers(channel_handle, start=start, count=count, sort=sort, search=search)

List followers of a video channel

### Example

* OAuth Authentication (OAuth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str | Sort followers by criteria (optional)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)

    try:
        # List followers of a video channel
        api_response = api_instance.get_video_channel_followers(channel_handle, start=start, count=count, sort=sort, search=search)
        print("The response of VideoChannelsApi->get_video_channel_followers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->get_video_channel_followers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort followers by criteria | [optional] 
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

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

# **get_video_channel_videos**
> VideoListResponse get_video_channel_videos(channel_handle, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos of a video channel

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    category_one_of = peertube_api_client.GetAccountVideosCategoryOneOfParameter() # GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories)) (optional)
    is_live = True # bool | whether or not the video is a live (optional)
    tags_one_of = peertube_api_client.GetAccountVideosTagsOneOfParameter() # GetAccountVideosTagsOneOfParameter | tag(s) of the video (optional)
    tags_all_of = peertube_api_client.GetAccountVideosTagsAllOfParameter() # GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video (optional)
    licence_one_of = peertube_api_client.GetAccountVideosLicenceOneOfParameter() # GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences)) (optional)
    language_one_of = peertube_api_client.GetAccountVideosLanguageOneOfParameter() # GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language (optional)
    nsfw = 'nsfw_example' # str | whether to include nsfw videos, if any (optional)
    is_local = True # bool | **PeerTube >= 4.0** Display only local or remote videos (optional)
    include = 56 # int | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES  (optional)
    privacy_one_of = peertube_api_client.VideoPrivacySet() # VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies (optional)
    has_hls_files = True # bool | **PeerTube >= 4.0** Display only videos that have HLS files (optional)
    has_webtorrent_files = True # bool | **PeerTube >= 4.0** Display only videos that have WebTorrent files (optional)
    skip_count = 'false' # str | if you don't need the `total` in the response (optional) (default to 'false')
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = 'sort_example' # str |  (optional)
    exclude_already_watched = True # bool | Whether or not to exclude videos that are in the user's video history (optional)

    try:
        # List videos of a video channel
        api_response = api_instance.get_video_channel_videos(channel_handle, category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of VideoChannelsApi->get_video_channel_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->get_video_channel_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **category_one_of** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **is_live** | **bool**| whether or not the video is a live | [optional] 
 **tags_one_of** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] 
 **tags_all_of** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] 
 **licence_one_of** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **language_one_of** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] 
 **nsfw** | **str**| whether to include nsfw videos, if any | [optional] 
 **is_local** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] 
 **include** | **int**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] 
 **privacy_one_of** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] 
 **has_hls_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] 
 **has_webtorrent_files** | **bool**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] 
 **skip_count** | **str**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to &#39;false&#39;]
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**|  | [optional] 
 **exclude_already_watched** | **bool**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

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

# **get_video_channels**
> VideoChannelList get_video_channels(start=start, count=count, sort=sort)

List video channels

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_list import VideoChannelList
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # List video channels
        api_response = api_instance.get_video_channels(start=start, count=count, sort=sort)
        print("The response of VideoChannelsApi->get_video_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->get_video_channels: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

### Return type

[**VideoChannelList**](VideoChannelList.md)

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

# **put_video_channel**
> put_video_channel(channel_handle, video_channel_update=video_channel_update)

Update a video channel

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_channel_update import VideoChannelUpdate
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
    api_instance = peertube_api_client.VideoChannelsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    video_channel_update = peertube_api_client.VideoChannelUpdate() # VideoChannelUpdate |  (optional)

    try:
        # Update a video channel
        api_instance.put_video_channel(channel_handle, video_channel_update=video_channel_update)
    except Exception as e:
        print("Exception when calling VideoChannelsApi->put_video_channel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_handle** | **str**| The video channel handle | 
 **video_channel_update** | [**VideoChannelUpdate**](VideoChannelUpdate.md)|  | [optional] 

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

