# peertube_api_client.VideoPlaylistsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_playlist**](VideoPlaylistsApi.md#add_playlist) | **POST** /api/v1/video-playlists | Create a video playlist
[**add_video_playlist_video**](VideoPlaylistsApi.md#add_video_playlist_video) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
[**api_v1_accounts_name_video_playlists_get**](VideoPlaylistsApi.md#api_v1_accounts_name_video_playlists_get) | **GET** /api/v1/accounts/{name}/video-playlists | List playlists of an account
[**api_v1_users_me_video_playlists_videos_exist_get**](VideoPlaylistsApi.md#api_v1_users_me_video_playlists_videos_exist_get) | **GET** /api/v1/users/me/video-playlists/videos-exist | Check video exists in my playlists
[**api_v1_video_channels_channel_handle_video_playlists_get**](VideoPlaylistsApi.md#api_v1_video_channels_channel_handle_video_playlists_get) | **GET** /api/v1/video-channels/{channelHandle}/video-playlists | List playlists of a channel
[**api_v1_video_playlists_playlist_id_delete**](VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_delete) | **DELETE** /api/v1/video-playlists/{playlistId} | Delete a video playlist
[**api_v1_video_playlists_playlist_id_get**](VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_get) | **GET** /api/v1/video-playlists/{playlistId} | Get a video playlist
[**api_v1_video_playlists_playlist_id_put**](VideoPlaylistsApi.md#api_v1_video_playlists_playlist_id_put) | **PUT** /api/v1/video-playlists/{playlistId} | Update a video playlist
[**del_video_playlist_video**](VideoPlaylistsApi.md#del_video_playlist_video) | **DELETE** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Delete an element from a playlist
[**get_playlist_privacy_policies**](VideoPlaylistsApi.md#get_playlist_privacy_policies) | **GET** /api/v1/video-playlists/privacies | List available playlist privacy policies
[**get_playlists**](VideoPlaylistsApi.md#get_playlists) | **GET** /api/v1/video-playlists | List video playlists
[**get_video_playlist_videos**](VideoPlaylistsApi.md#get_video_playlist_videos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist
[**put_video_playlist_video**](VideoPlaylistsApi.md#put_video_playlist_video) | **PUT** /api/v1/video-playlists/{playlistId}/videos/{playlistElementId} | Update a playlist element
[**reorder_video_playlist**](VideoPlaylistsApi.md#reorder_video_playlist) | **POST** /api/v1/video-playlists/{playlistId}/videos/reorder | Reorder a playlist


# **add_playlist**
> AddPlaylist200Response add_playlist(display_name, thumbnailfile=thumbnailfile, privacy=privacy, description=description, video_channel_id=video_channel_id)

Create a video playlist

If the video playlist is set as public, `videoChannelId` is mandatory.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_playlist200_response import AddPlaylist200Response
from peertube_api_client.models.video_playlist_privacy_set import VideoPlaylistPrivacySet
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    display_name = 'display_name_example' # str | Video playlist display name
    thumbnailfile = None # bytearray | Video playlist thumbnail file (optional)
    privacy = peertube_api_client.VideoPlaylistPrivacySet() # VideoPlaylistPrivacySet |  (optional)
    description = 'description_example' # str | Video playlist description (optional)
    video_channel_id = 56 # int |  (optional)

    try:
        # Create a video playlist
        api_response = api_instance.add_playlist(display_name, thumbnailfile=thumbnailfile, privacy=privacy, description=description, video_channel_id=video_channel_id)
        print("The response of VideoPlaylistsApi->add_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->add_playlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| Video playlist display name | 
 **thumbnailfile** | **bytearray**| Video playlist thumbnail file | [optional] 
 **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] 
 **description** | **str**| Video playlist description | [optional] 
 **video_channel_id** | [**int**](int.md)|  | [optional] 

### Return type

[**AddPlaylist200Response**](AddPlaylist200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_playlist_video**
> AddVideoPlaylistVideo200Response add_video_playlist_video(playlist_id, add_video_playlist_video_request=add_video_playlist_video_request)

Add a video in a playlist

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.add_video_playlist_video200_response import AddVideoPlaylistVideo200Response
from peertube_api_client.models.add_video_playlist_video_request import AddVideoPlaylistVideoRequest
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    add_video_playlist_video_request = peertube_api_client.AddVideoPlaylistVideoRequest() # AddVideoPlaylistVideoRequest |  (optional)

    try:
        # Add a video in a playlist
        api_response = api_instance.add_video_playlist_video(playlist_id, add_video_playlist_video_request=add_video_playlist_video_request)
        print("The response of VideoPlaylistsApi->add_video_playlist_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->add_video_playlist_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **add_video_playlist_video_request** | [**AddVideoPlaylistVideoRequest**](AddVideoPlaylistVideoRequest.md)|  | [optional] 

### Return type

[**AddVideoPlaylistVideo200Response**](AddVideoPlaylistVideo200Response.md)

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

# **api_v1_accounts_name_video_playlists_get**
> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response api_v1_accounts_name_video_playlists_get(name, start=start, count=count, sort=sort, search=search, playlist_type=playlist_type)

List playlists of an account

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    name = 'chocobozzz | chocobozzz@example.org' # str | The username or handle of the account
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    search = 'search_example' # str | Plain text search, applied to various parts of the model depending on endpoint (optional)
    playlist_type = peertube_api_client.VideoPlaylistTypeSet() # VideoPlaylistTypeSet |  (optional)

    try:
        # List playlists of an account
        api_response = api_instance.api_v1_accounts_name_video_playlists_get(name, start=start, count=count, sort=sort, search=search, playlist_type=playlist_type)
        print("The response of VideoPlaylistsApi->api_v1_accounts_name_video_playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_accounts_name_video_playlists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The username or handle of the account | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **search** | **str**| Plain text search, applied to various parts of the model depending on endpoint | [optional] 
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

# **api_v1_users_me_video_playlists_videos_exist_get**
> ApiV1UsersMeVideoPlaylistsVideosExistGet200Response api_v1_users_me_video_playlists_videos_exist_get(video_ids)

Check video exists in my playlists

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.api_v1_users_me_video_playlists_videos_exist_get200_response import ApiV1UsersMeVideoPlaylistsVideosExistGet200Response
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    video_ids = [56] # List[int] | The video ids to check

    try:
        # Check video exists in my playlists
        api_response = api_instance.api_v1_users_me_video_playlists_videos_exist_get(video_ids)
        print("The response of VideoPlaylistsApi->api_v1_users_me_video_playlists_videos_exist_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_users_me_video_playlists_videos_exist_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_ids** | [**List[int]**](int.md)| The video ids to check | 

### Return type

[**ApiV1UsersMeVideoPlaylistsVideosExistGet200Response**](ApiV1UsersMeVideoPlaylistsVideosExistGet200Response.md)

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    channel_handle = 'my_username | my_username@example.com' # str | The video channel handle
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    playlist_type = peertube_api_client.VideoPlaylistTypeSet() # VideoPlaylistTypeSet |  (optional)

    try:
        # List playlists of a channel
        api_response = api_instance.api_v1_video_channels_channel_handle_video_playlists_get(channel_handle, start=start, count=count, sort=sort, playlist_type=playlist_type)
        print("The response of VideoPlaylistsApi->api_v1_video_channels_channel_handle_video_playlists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_video_channels_channel_handle_video_playlists_get: %s\n" % e)
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

# **api_v1_video_playlists_playlist_id_delete**
> api_v1_video_playlists_playlist_id_delete(playlist_id)

Delete a video playlist

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id

    try:
        # Delete a video playlist
        api_instance.api_v1_video_playlists_playlist_id_delete(playlist_id)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_video_playlists_playlist_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 

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

# **api_v1_video_playlists_playlist_id_get**
> VideoPlaylist api_v1_video_playlists_playlist_id_get(playlist_id)

Get a video playlist

### Example

```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_playlist import VideoPlaylist
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id

    try:
        # Get a video playlist
        api_response = api_instance.api_v1_video_playlists_playlist_id_get(playlist_id)
        print("The response of VideoPlaylistsApi->api_v1_video_playlists_playlist_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_video_playlists_playlist_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 

### Return type

[**VideoPlaylist**](VideoPlaylist.md)

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

# **api_v1_video_playlists_playlist_id_put**
> api_v1_video_playlists_playlist_id_put(playlist_id, display_name=display_name, thumbnailfile=thumbnailfile, privacy=privacy, description=description, video_channel_id=video_channel_id)

Update a video playlist

If the video playlist is set as public, the playlist must have a assigned channel.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_playlist_privacy_set import VideoPlaylistPrivacySet
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    display_name = 'display_name_example' # str | Video playlist display name (optional)
    thumbnailfile = None # bytearray | Video playlist thumbnail file (optional)
    privacy = peertube_api_client.VideoPlaylistPrivacySet() # VideoPlaylistPrivacySet |  (optional)
    description = 'description_example' # str | Video playlist description (optional)
    video_channel_id = 56 # int |  (optional)

    try:
        # Update a video playlist
        api_instance.api_v1_video_playlists_playlist_id_put(playlist_id, display_name=display_name, thumbnailfile=thumbnailfile, privacy=privacy, description=description, video_channel_id=video_channel_id)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->api_v1_video_playlists_playlist_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **display_name** | **str**| Video playlist display name | [optional] 
 **thumbnailfile** | **bytearray**| Video playlist thumbnail file | [optional] 
 **privacy** | [**VideoPlaylistPrivacySet**](VideoPlaylistPrivacySet.md)|  | [optional] 
 **description** | **str**| Video playlist description | [optional] 
 **video_channel_id** | [**int**](int.md)|  | [optional] 

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

# **del_video_playlist_video**
> del_video_playlist_video(playlist_id, playlist_element_id)

Delete an element from a playlist

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    playlist_element_id = 56 # int | Playlist element id

    try:
        # Delete an element from a playlist
        api_instance.del_video_playlist_video(playlist_id, playlist_element_id)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->del_video_playlist_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **playlist_element_id** | **int**| Playlist element id | 

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

# **get_playlist_privacy_policies**
> List[str] get_playlist_privacy_policies()

List available playlist privacy policies

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)

    try:
        # List available playlist privacy policies
        api_response = api_instance.get_playlist_privacy_policies()
        print("The response of VideoPlaylistsApi->get_playlist_privacy_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->get_playlist_privacy_policies: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **get_playlists**
> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response get_playlists(start=start, count=count, sort=sort, playlist_type=playlist_type)

List video playlists

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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    playlist_type = peertube_api_client.VideoPlaylistTypeSet() # VideoPlaylistTypeSet |  (optional)

    try:
        # List video playlists
        api_response = api_instance.get_playlists(start=start, count=count, sort=sort, playlist_type=playlist_type)
        print("The response of VideoPlaylistsApi->get_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->get_playlists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_video_playlist_videos**
> VideoListResponse get_video_playlist_videos(playlist_id, start=start, count=count)

List videos of a playlist

### Example

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


# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)

    try:
        # List videos of a playlist
        api_response = api_instance.get_video_playlist_videos(playlist_id, start=start, count=count)
        print("The response of VideoPlaylistsApi->get_video_playlist_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->get_video_playlist_videos: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]

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

# **put_video_playlist_video**
> put_video_playlist_video(playlist_id, playlist_element_id, put_video_playlist_video_request=put_video_playlist_video_request)

Update a playlist element

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.put_video_playlist_video_request import PutVideoPlaylistVideoRequest
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    playlist_element_id = 56 # int | Playlist element id
    put_video_playlist_video_request = peertube_api_client.PutVideoPlaylistVideoRequest() # PutVideoPlaylistVideoRequest |  (optional)

    try:
        # Update a playlist element
        api_instance.put_video_playlist_video(playlist_id, playlist_element_id, put_video_playlist_video_request=put_video_playlist_video_request)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->put_video_playlist_video: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **playlist_element_id** | **int**| Playlist element id | 
 **put_video_playlist_video_request** | [**PutVideoPlaylistVideoRequest**](PutVideoPlaylistVideoRequest.md)|  | [optional] 

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

# **reorder_video_playlist**
> reorder_video_playlist(playlist_id, reorder_video_playlist_request=reorder_video_playlist_request)

Reorder a playlist

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.reorder_video_playlist_request import ReorderVideoPlaylistRequest
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
    api_instance = peertube_api_client.VideoPlaylistsApi(api_client)
    playlist_id = 56 # int | Playlist id
    reorder_video_playlist_request = peertube_api_client.ReorderVideoPlaylistRequest() # ReorderVideoPlaylistRequest |  (optional)

    try:
        # Reorder a playlist
        api_instance.reorder_video_playlist(playlist_id, reorder_video_playlist_request=reorder_video_playlist_request)
    except Exception as e:
        print("Exception when calling VideoPlaylistsApi->reorder_video_playlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **int**| Playlist id | 
 **reorder_video_playlist_request** | [**ReorderVideoPlaylistRequest**](ReorderVideoPlaylistRequest.md)|  | [optional] 

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

