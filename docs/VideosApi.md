# peertube_api_client.VideosApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_video_playlist_video**](VideosApi.md#add_video_playlist_video) | **POST** /api/v1/video-playlists/{playlistId}/videos | Add a video in a playlist
[**api_v1_users_me_subscriptions_videos_get**](VideosApi.md#api_v1_users_me_subscriptions_videos_get) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user
[**api_v1_users_me_videos_get**](VideosApi.md#api_v1_users_me_videos_get) | **GET** /api/v1/users/me/videos | Get videos of my user
[**api_v1_users_me_videos_imports_get**](VideosApi.md#api_v1_users_me_videos_imports_get) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
[**get_video_playlist_videos**](VideosApi.md#get_video_playlist_videos) | **GET** /api/v1/video-playlists/{playlistId}/videos | List videos of a playlist


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
    api_instance = peertube_api_client.VideosApi(api_client)
    playlist_id = 56 # int | Playlist id
    add_video_playlist_video_request = peertube_api_client.AddVideoPlaylistVideoRequest() # AddVideoPlaylistVideoRequest |  (optional)

    try:
        # Add a video in a playlist
        api_response = api_instance.add_video_playlist_video(playlist_id, add_video_playlist_video_request=add_video_playlist_video_request)
        print("The response of VideosApi->add_video_playlist_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->add_video_playlist_video: %s\n" % e)
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

# **api_v1_users_me_subscriptions_videos_get**
> VideoListResponse api_v1_users_me_subscriptions_videos_get(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)

List videos of subscriptions of my user

### Example

* OAuth Authentication (OAuth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with peertube_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = peertube_api_client.VideosApi(api_client)
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
        # List videos of subscriptions of my user
        api_response = api_instance.api_v1_users_me_subscriptions_videos_get(category_one_of=category_one_of, is_live=is_live, tags_one_of=tags_one_of, tags_all_of=tags_all_of, licence_one_of=licence_one_of, language_one_of=language_one_of, nsfw=nsfw, is_local=is_local, include=include, privacy_one_of=privacy_one_of, has_hls_files=has_hls_files, has_webtorrent_files=has_webtorrent_files, skip_count=skip_count, start=start, count=count, sort=sort, exclude_already_watched=exclude_already_watched)
        print("The response of VideosApi->api_v1_users_me_subscriptions_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->api_v1_users_me_subscriptions_videos_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_me_videos_get**
> VideoListResponse api_v1_users_me_videos_get(start=start, count=count, sort=sort)

Get videos of my user

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
    api_instance = peertube_api_client.VideosApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)

    try:
        # Get videos of my user
        api_response = api_instance.api_v1_users_me_videos_get(start=start, count=count, sort=sort)
        print("The response of VideosApi->api_v1_users_me_videos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->api_v1_users_me_videos_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 

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

# **api_v1_users_me_videos_imports_get**
> VideoImportsList api_v1_users_me_videos_imports_get(start=start, count=count, sort=sort, target_url=target_url, video_channel_sync_id=video_channel_sync_id, search=search)

Get video imports of my user

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import peertube_api_client
from peertube_api_client.models.video_imports_list import VideoImportsList
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
    api_instance = peertube_api_client.VideosApi(api_client)
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)
    sort = '-createdAt' # str | Sort column (optional)
    target_url = 'target_url_example' # str | Filter on import target URL (optional)
    video_channel_sync_id = 3.4 # float | Filter on imports created by a specific channel synchronization (optional)
    search = 'search_example' # str | Search in video names (optional)

    try:
        # Get video imports of my user
        api_response = api_instance.api_v1_users_me_videos_imports_get(start=start, count=count, sort=sort, target_url=target_url, video_channel_sync_id=video_channel_sync_id, search=search)
        print("The response of VideosApi->api_v1_users_me_videos_imports_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->api_v1_users_me_videos_imports_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Offset used to paginate results | [optional] 
 **count** | **int**| Number of items to return | [optional] [default to 15]
 **sort** | **str**| Sort column | [optional] 
 **target_url** | **str**| Filter on import target URL | [optional] 
 **video_channel_sync_id** | **float**| Filter on imports created by a specific channel synchronization | [optional] 
 **search** | **str**| Search in video names | [optional] 

### Return type

[**VideoImportsList**](VideoImportsList.md)

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
    api_instance = peertube_api_client.VideosApi(api_client)
    playlist_id = 56 # int | Playlist id
    start = 56 # int | Offset used to paginate results (optional)
    count = 15 # int | Number of items to return (optional) (default to 15)

    try:
        # List videos of a playlist
        api_response = api_instance.get_video_playlist_videos(playlist_id, start=start, count=count)
        print("The response of VideosApi->get_video_playlist_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VideosApi->get_video_playlist_videos: %s\n" % e)
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

